"""Build the claude.ai version of Wordshelf (runs on the visitor's Claude account via the artifact `sample` capability).
Usage: python3 tools/build-claude.py OUT.html"""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
s = (root / "index.html").read_text()

def sub(old, new, count=1):
    global s
    assert s.count(old) == count, (old, s.count(old))
    s = s.replace(old, new)

# only the Claude account mode here: other services can't be reached from inside claude.ai
s = re.sub(r'(<select id="modeSel"[^>]*>).*?(</select>)', r'\1<option value="account">Claude account</option>\2', s, flags=re.S)
sub('<link rel="manifest" href="manifest.webmanifest">', '')
# the "open on claude.ai" box isn't needed when we're already there
sub('$("#accountBox").hidden=m!=="account";', '$("#accountBox").hidden=true;')
sub('account:"Have a Claude account (claude.ai) but no API key? Use the claude.ai version of Wordshelf, which runs on your account.",',
    'account:"Runs on your Claude account. No key needed: Claude reads handwriting, phrases and translations, and writes example sentences for every word. It counts toward your Claude plan\'s usage.",')
sub('var mode=(()=>{try{return localStorage.getItem(MODE_KEY)}catch{return null}})()||"gemini";', 'var mode="account";')
# the account counts as a Claude "key" so sentences and translations use it automatically
sub('const getKey=(m=mode)=>{', 'const getKey=(m=mode)=>{if(m==="claude"||m==="account")return "__account__";')
sub('if(mode==="account"){setStatus("With a Claude account, scanning happens on claude.ai. Use the Open Wordshelf on claude.ai button below.",true);return null}',
    'if(mode==="account"){setStatus(spin(label));return askAccount(prompt,images,true)}')
sub('async function askClaude(key,prompt,images){\n', 'async function askClaude(key,prompt,images){\n  if(key==="__account__") return askAccount(prompt,images,true);\n')
sub('async function askClaudeText(key,prompt){\n', 'async function askClaudeText(key,prompt){\n  if(key==="__account__") return askAccount(prompt,[],false);\n')

helper = r'''
/* Claude account (claude.ai): the page asks Claude through the viewer's own account */
const samplerP=(window.claude?.use?window.claude.use("sample"):Promise.resolve(null)).catch(()=>null);
const SAMPLE_ERR={not_granted:"Allow Wordshelf to use Claude (the prompt at the top) to read words and write sentences.",
  rate_limited:"Claude is busy for your account right now. Wait a minute and try again.",
  sampling_disabled:"Using Claude from pages is turned off for your account.",session_expired:"Your claude.ai session expired. Reload the page.",
  prompt_too_large:"That's too much at once. Split the photo or list into smaller parts.",image_rejected:"Claude couldn't open that image. Try a screenshot or a smaller photo.",
  images_unavailable:"Images can't be sent from this view. Type the words instead.",refused:"Claude couldn't process that. Try a different image."};
async function askAccount(prompt,images,structured){
  const sample=await samplerP;
  if(!sample) return fail("Claude isn't available here. Open this page on claude.ai while signed in.");
  try{
    const blobs=[];
    for(const f of images||[]){const p=await prepImage(f);blobs.push(new Blob([Uint8Array.from(atob(p.data),c=>c.charCodeAt(0))],{type:p.media_type}))}
    const ask=(structured?prompt+"\n\nReply with only JSON matching this schema (no other text):\n"+JSON.stringify(SCHEMA):prompt);
    const {text}=await sample(ask,{images:blobs.length?blobs:undefined,modelTier:"default"});
    return parseJSONReply(text)||fail("Claude's answer wasn't in the expected format. Try again.");
  }catch(e){
    if(e&&e.code==="cancelled") return null;
    return fail(SAMPLE_ERR[e?.code]||("Claude couldn't answer right now"+(e?.message?": "+e.message:"")+". Try again."));
  }
}
'''
sub('async function askClaude(key,prompt,images){', helper + 'async function askClaude(key,prompt,images){')
(pathlib.Path(sys.argv[1])).write_text(s)
print("ok", len(s))
