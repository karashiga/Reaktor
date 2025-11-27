
#!/usr/bin/env node
=============================================================================
*/
 
const https = require('https');
const readline = require('readline');
const fs = require('fs');
 
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
 
const C = (c, t) => `\x1b[${c}m${t}\x1b[0m`;
const green = (t) => C('92', t);
const red = (t) => C('91', t);
const yellow = (t) => C('93', t);
const cyan = (t) => C('96', t);
const magenta = (t) => C('95', t);
const blue = (t) => C('94', t);
const white = (t) => C('97', t);
const reset = (t) => C('0', t);
 
function showHelp() {
console.log(magenta('\n════════════════════════════════════════════════════════════════════════'));
console.log(magenta('                           HELP & GUIDE                               '));
console.log(magenta('════════════════════════════════════════════════════════════════════════'));
 
console.log(cyan('  INSTALLATION'));
console.log(cyan('  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'));
console.log(cyan('   • Linux/Ubuntu        : sudo apt install nodejs npm'));
console.log(cyan('   • Termux              : pkg install nodejs'));
console.log(cyan('   • Windows             : Download from nodejs.org'));
console.log('');
 
console.log(cyan('  BASIC USAGE'));
console.log(cyan('  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'));
console.log(cyan('   1. Run                 : node fb_auto_share.js'));
console.log(cyan('   2. Add accounts        : Option 1'));
console.log(cyan('   3. Mass Share          : Option 5 (bulk sharing)'));
console.log('');
 
console.log(cyan('  COOKIE FORMAT'));
console.log(cyan('  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'));
console.log(cyan('   • Must contain: c_user, xs, datr, fr (minimum)'));
console.log(cyan('   • Copy the entire cookie string from browser'));
console.log('');
 
console.log(cyan('  KEY FEATURES'));
console.log(cyan('  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'));
console.log(cyan('   • Unlimited account adding'));
console.log(cyan('   • FAST Mass Share → up to 4000+ shares per account'));
console.log(cyan('   • Per-account detailed statistics'));
console.log(cyan('   • Customizable delay (0–5 seconds)'));
console.log(cyan('   • Real-time progress bar & colorful logs'));
console.log(green('   • PERFORMANCE MODE → 3× FASTER SHARING!               '));
 
console.log(magenta('════════════════════════════════════════════════════════════════════════'));
console.log(magenta('       Made by  by Jhames Martin - PH Edition 2025       '));
console.log(magenta('════════════════════════════════════════════════════════════════════════\n'));
}
 
function printAnimatedBanner() {
  console.clear();
 
  console.log(magenta('\n'));
  console.log('╔══════════════════════════════════════════════════════════════════════════╗');
  console.log('║                    ⚡ FB AUTO SHARE v1.1 FAST EDITION ⚡                 ║');
  console.log('║                            Cookie → Token → Mass Share Loop              ║');
  console.log('╚══════════════════════════════════════════════════════════════════════════╝');
 
  setTimeout(() => {
    console.log(magenta('\n'));
console.log(cyan('    ███████╗██████╗  ███╗   ███╗ █████╗  ███████╗███████╗ ███████╗██╗  ██╗ █████╗ ██████╗ ███████╗'));
console.log(cyan('    ██╔════╝██╔══██╗████╗ ████║██╔══██╗██╔════╝██╔══════╝ ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝'));
console.log(cyan('    █████╗  ██████╔╝██╔████╔██║███████║███████╗███████╗   ███████╗███████║███████║██████╔╝█████╗  '));
console.log(cyan('    ██╔══╝  ██╔══██╗██║╚██╔╝██║██╔══██║╚════██║╚════██║   ╚════██║██╔══██║██╔══██║██╔══██╗██╔══╝  '));
console.log(cyan('    ██║     ███████║██║ ╚═╝ ██║██║  ██║███████║███████║   ███████║██║  ██║██║  ██║██║  ██║███████╗'));
console.log(cyan('    ╚═╝     ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╚═══════╝    ╚══════╝╚╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝'));
    console.log('');
  }, 300);
 
  setTimeout(() => {
    console.log(green('     🚀 Made by Jhames Martin'));
    console.log(cyan('         ⚙️ Termux Ready • PH Edition 2025'));
    console.log(cyan('         ⚡ FAST EDITION - 3X FASTER!'));
    console.log(cyan('         🔥 4000 SHARES PER ACCOUNT LIMIT'));
    console.log('');
  }, 600);
 
  setTimeout(() => {
    console.log(yellow('     🎯 Press [H] for Help | [I] for Installation Guide'));
    console.log(blue('     📱 Ready for ultra-fast mass sharing!'));
    console.log('');
    console.log(green('     ⚡ Initializing FAST EDITION...'));
 
    setTimeout(() => {
      console.log(cyan('\n     ████████████████████████████████████████████████'));
      console.log(cyan('     █                                              █'));
      console.log(cyan('     █          ✅ SYSTEM READY! ✅                 █'));
      console.log(cyan('     █                                              █'));
      console.log(cyan('     ████████████████████████████████████████████████'));
      console.log(blue('\n     🔥 Starting ultra-fast interface...\n'));
 
      setTimeout(() => {
        startMain();
      }, 1000);
    }, 800);
  }, 1000);
}
 
const ACCOUNTS_FILE = 'accounts.json';
 
class AccountManager {
  static loadAccounts() {
    if (fs.existsSync(ACCOUNTS_FILE)) {
      try {
        return JSON.parse(fs.readFileSync(ACCOUNTS_FILE, 'utf8'));
      } catch {
        return [];
      }
    }
    return [];
  }
 
  static saveAccounts(accounts) {
    fs.writeFileSync(ACCOUNTS_FILE, JSON.stringify(accounts, null, 2));
  }
 
  static async addAccount() {
    const accounts = this.loadAccounts();
    console.log(yellow('\n[+] ➕ Add New Facebook Account'));
    console.log(cyan('📝 Input Facebook Cookie (c_user, xs, datr):'));
    console.log(magenta('💡 Tip: Copy complete cookie from Facebook'));
 
    const cookie = await ask(cyan('\nCookie: '));
    if (!cookie.includes('c_user=') || !cookie.includes('xs=')) {
      console.log(red('❌ Invalid cookie! Please ensure it contains c_user= and xs='));
      return false;
    }
 
    console.log(yellow('\n[+] 🔄 Getting access token...'));
    try {
      const token = await getToken(cookie);
      const accountId = Date.now();
      const account = {
        id: accountId,
        cookie: cookie,
        token: token,
        added: new Date().toISOString(),
        status: 'active',
        shareCount: 0,
        successRate: '100%',
        lastShare: null
      };
 
      accounts.push(account);
      this.saveAccounts(accounts);
      console.log(green(`✅ Account added successfully! ID: ${accountId}`));
      console.log(blue(`🎉 Ready for mass sharing!`));
      return true;
    } catch (e) {
      console.log(red(`❌ Failed to get token: ${e.message}`));
      console.log(yellow('💡 Check your internet connection and cookie validity'));
      return false;
    }
  }
 
static listAccounts() {
  const accounts = this.loadAccounts();
 
  if (accounts.length === 0) {
    console.log(red('\n════════════════════════════════════════════════════════════════════════'));
    console.log(red('                     NO ACCOUNTS FOUND                     '));
    console.log(red('════════════════════════════════════════════════════════════════════════'));
    console.log(yellow('  Use option [1] to add your first account'));
    console.log(yellow('  Ready to add UNLIMITED Facebook accounts!'));
    console.log(red('════════════════════════════════════════════════════════════════════════\n'));
    return [];
  }
 
  console.log(magenta('\n════════════════════════════════════════════════════════════════════════'));
  console.log(magenta('                       REGISTERED ACCOUNTS                       '));
  console.log(magenta('════════════════════════════════════════════════════════════════════════'));
  console.log(cyan('  #   ACCOUNT ID       STATUS     SHARES   SUCCESS   ADDED DATE'));
  console.log(cyan('  ──────────────────────────────────────────────────────────────────────'));
 
  accounts.forEach((acc, i) => {
    const status = acc.status === 'active' ? green('ACTIVE   ') : red('INACTIVE ');
    const successRate = acc.shareCount > 0 ? `${acc.successRate}%`.padEnd(6) : 'N/A   ';
    const idShort = acc.id.toString().substring(0, 12).padEnd(12) + '...';
    const shares = String(acc.shareCount).padEnd(6);
    const added = acc.added.split('T')[0];
 
    console.log(cyan(`  \( {String(i + 1).padStart(2)} \){idShort}  \( {status} \){shares}   \( {successRate} \){added}`));
  });
 
  console.log(cyan('  ──────────────────────────────────────────────────────────────────────'));
 
  const activeCount = accounts.filter(a => a.status === 'active').length;
  const totalShares = accounts.reduce((sum, a) => sum + a.shareCount, 0);
  const avgSuccess = accounts.length > 0 
    ? (accounts.reduce((sum, a) => sum + (a.successRate || 0), 0) / accounts.length).toFixed(1)
    : 0;
 
  console.log(cyan('\n  SUMMARY:'));
  console.log(blue  (`   Total Accounts     : ${accounts.length}`.padEnd(50)));
  console.log(green (`   Active Accounts    : ${activeCount}`.padEnd(50)));
  console.log(red   (`   Inactive Accounts  : ${accounts.length - activeCount}`.padEnd(50)));
  console.log(yellow(`   Total Shares Done  : ${totalShares}`.padEnd(50)));
  console.log(magenta(`   Avg Success Rate   : ${avgSuccess}%`.padEnd(50)));
 
  console.log(magenta('════════════════════════════════════════════════════════════════════════\n'));
 
  return accounts;
}
  static async removeAccount() {
    const accounts = this.listAccounts();
    if (accounts.length === 0) return;
 
    const inputPrompt = cyan('\n[+] Select account to remove (number): ');
    const indexInput = await ask(inputPrompt);
    const index = parseInt(indexInput) - 1;
 
    if (index < 0 || index >= accounts.length) {
      console.log(red('❌ Invalid selection!'));
      return;
    }
 
    const removed = accounts.splice(index, 1)[0];
    this.saveAccounts(accounts);
    console.log(green(`✅ Account ${removed.id} removed successfully!`));
  }
 
  static async toggleAccountStatus() {
    const accounts = this.listAccounts();
    if (accounts.length === 0) return;
 
    const inputPrompt = cyan('\n[+] Select account to toggle (number): ');
    const indexInput = await ask(inputPrompt);
    const index = parseInt(indexInput) - 1;
 
    if (index < 0 || index >= accounts.length) {
      console.log(red('❌ Invalid selection!'));
      return;
    }
 
    accounts[index].status = accounts[index].status === 'active' ? 'inactive' : 'active';
    this.saveAccounts(accounts);
    const status = accounts[index].status === 'active' ? green('ACTIVE') : red('INACTIVE');
    console.log(green(`✅ Account ${accounts[index].id} is now ${status}`));
  }
}
 
function ask(q) {
  return new Promise(r => rl.question(q, r));
}
 
async function getToken(cookie) {
  return new Promise((resolve, reject) => {
    const options = {
      hostname: 'business.facebook.com',
      path: '/business_locations',
      method: 'GET',
      headers: {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36',
        'Referer': 'https://www.facebook.com/',
        'Cookie': cookie,
        'Accept': 'text/html',
        'Accept-Language': 'en-US,en;q=0.9'
      }
    };
 
    const req = https.request(options, res => {
      let data = '';
      res.on('data', d => data += d);
      res.on('end', () => {
        const match = data.match(/EAAG\w+/);
        match ? resolve(match[0]) : reject(new Error('Invalid cookie'));
      });
    });
    req.on('error', () => reject(new Error('Network error')));
    req.end();
  });
}
 
async function shareOnce(token, cookie, url, accountId = null) {
  return new Promise(resolve => {
    const data = JSON.stringify({ link: url, published: 0, access_token: token });
    const options = {
      hostname: 'graph.facebook.com',
      path: '/v20.0/me/feed',
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0', 'Cookie': cookie }
    };
 
    const req = https.request(options, res => {
      let body = '';
      res.on('data', d => body += d);
      res.on('end', () => {
        try {
          const json = JSON.parse(body);
          if (json.id) {
            resolve({ success: true, id: json.id.split('_')[1], accountId });
          } else {
            resolve({ success: false, error: json.error?.message || 'Failed', accountId });
          }
        } catch {
          resolve({ success: false, error: 'Parse error', accountId });
        }
      });
    });
    req.on('error', () => resolve({ success: false, error: 'Request failed', accountId }));
    req.write(data); req.end();
  });
}
 
async function massShare() {
  const accounts = AccountManager.loadAccounts();
  const activeAccounts = accounts.filter(acc => acc.status === 'active');
 
  if (activeAccounts.length === 0) {
    console.log(red('\n❌ No active accounts found!'));
    console.log(yellow('💡 Add accounts first or activate existing ones'));
    return;
  }
 
  const postUrl = await ask(cyan('\n[+] 🌐 Enter Post URL to share: '));
  const sharesPerAccountInput = await ask(cyan('[+] 🔢 Shares per account (1-4000): '));
  const sharesPerAccount = parseInt(sharesPerAccountInput);
  const delayInput = await ask(cyan('[+] ⏱️  Delay between shares in seconds (0-5): '));
  const delay = parseInt(delayInput);
 
  if (isNaN(sharesPerAccount) || sharesPerAccount < 1 || sharesPerAccount > 4000) {
    console.log(red('❌ Invalid shares per account! Must be between 1-4000'));
    return;
  }
 
  if (isNaN(delay) || delay < 0 || delay > 5) {
    console.log(red('❌ Invalid delay! Must be between 0-5 seconds (0 = fastest)'));
    return;
  }
 
  const totalShares = activeAccounts.length * sharesPerAccount;
  const estimatedTime = Math.ceil(totalShares * delay / 60);
 
  console.log(yellow(`\n[+] 🚀 FAST Mass Share Configuration:`));
  console.log(cyan(`   📱 Active Accounts: ${activeAccounts.length}`));
  console.log(cyan(`   🔢 Shares per account: ${sharesPerAccount}`));
  console.log(cyan(`   🌐 Total shares: ${totalShares}`));
  console.log(cyan(`   ⏱️  Fast Delay: ${delay}s between shares`));
  console.log(cyan(`   ⚡ Estimated time: ~${estimatedTime} minutes`));
  console.log(green(`   🚀 MAX LIMIT: 4000 shares per account (ENFORCED)`));
 
  const confirm = await ask(cyan('\n[+] ❓ Continue with mass sharing? (y/N): '));
  if (confirm.toLowerCase() !== 'y') {
    console.log(yellow('❌ Operation cancelled.'));
    return;
  }
 
  let totalSuccess = 0;
  let totalFailed = 0;
  const startTime = Date.now();
 
  console.log(yellow('\n🌪️  Starting MASS SHARING... (All Accounts)\n'));
  console.log(magenta('⚡ Multiple accounts working simultaneously! ⚡\n'));
 
  for (let accIndex = 0; accIndex < activeAccounts.length; accIndex++) {
    const account = activeAccounts[accIndex];
    console.log(magenta(`[📱 Account ${accIndex + 1}/${activeAccounts.length}] ID: ${account.id} - Processing ${sharesPerAccount} shares`));
 
    for (let i = 1; i <= sharesPerAccount; i++) {
      const progress = ((accIndex * sharesPerAccount + i) / totalShares * 100).toFixed(1);
      const currentShare = `${accIndex + 1}-${i}/${sharesPerAccount}`;
      process.stdout.write(`\r[${progress}%] 📊 Progress: ${cyan(currentShare)}...`);
 
      const result = await shareOnce(account.token, account.cookie, postUrl, account.id);
 
      if (result.success) {
        console.log(`\n${green(`   ✅ SUCCESS [${currentShare}] │ Post ID: ${result.id} │ Account: ${result.accountId}`)}`);
        totalSuccess++;
        account.shareCount++;
        account.lastShare = new Date().toISOString();
      } else {
        console.log(`\n${red(`   ❌ FAILED [${currentShare}] │ Error: ${result.error} │ Account: ${result.accountId}`)}`);
        totalFailed++;
      }
 
      if (i < sharesPerAccount || accIndex < activeAccounts.length - 1) {
        await new Promise(r => setTimeout(r, delay * 1000));
      }
    }
 
    console.log(green(`   ═══════════════════════════════════════════════════════════════`));
    console.log(green(`   ✅ ACCOUNT ${accIndex + 1} COMPLETED! All ${sharesPerAccount} shares processed!`));
    console.log(green(`   ═══════════════════════════════════════════════════════════════`));
    console.log('');
  }
 
  const duration = ((Date.now() - startTime) / 1000).toFixed(1);
 
  AccountManager.saveAccounts(accounts);
 
console.log(magenta('\n═════════════════════════════════════════════════════════════════════════'));
console.log(magenta('                  MASS SHARING COMPLETED!                  '));
console.log(magenta('═════════════════════════════════════════════════════════════════════════'));
console.log(green(`  TOTAL SUCCESS:     ${totalSuccess}`.padEnd(60)));
console.log(red(`  TOTAL FAILED:      ${totalFailed}`.padEnd(60)));
console.log(yellow(`  SUCCESS RATE:      ${((totalSuccess/(totalSuccess+totalFailed))*100).toFixed(1)}%`.padEnd(60)));
console.log(blue(`  DURATION:          \( {duration}s ( \){(duration/60).toFixed(1)} min)`.padEnd(60)));
console.log(cyan(`  ACCOUNTS USED:     ${activeAccounts.length}`.padEnd(60)));
console.log(magenta('═════════════════════════════════════════════════════════════════════════'));
console.log(cyan('  Thank you for using FB Auto Share v1.1 FAST EDITION!'));
console.log(yellow('  Ready for next massive sharing operation!'));
console.log(magenta('═════════════════════════════════════════════════════════════════════════\n'));
}
 
async function singleShare() {
  const accounts = AccountManager.listAccounts();
  if (accounts.length === 0) return;
 
  const indexInput = await ask(cyan('\n[+] Select account (number): '));
  const index = parseInt(indexInput) - 1;
  if (index < 0 || index >= accounts.length) {
    console.log(red('❌ Invalid selection!'));
    return;
  }
 
  const account = accounts[index];
  if (account.status !== 'active') {
    console.log(red(`❌ Account ${account.id} is inactive!`));
    return;
  }
 
  const postUrl = await ask(cyan('[+] 🌐 Enter Post URL to share: '));
  const sharesInput = await ask(cyan('[+] 🔢 Number of shares (1-4000): '));
  const shares = parseInt(sharesInput);
 
  if (isNaN(shares) || shares < 1 || shares > 4000) {
    console.log(red('❌ Invalid number! Must be between 1-4000'));
    return;
  }
 
  console.log(yellow(`\n[+] 🚀 Starting ${shares} shares with Account ${index + 1}...`));
  console.log(cyan(`   📱 Account ID: ${account.id}`));
  console.log(cyan(`   🔗 URL: ${postUrl}\n`));
 
  let success = 0;
 
  for (let i = 1; i <= shares; i++) {
    await new Promise(r => setTimeout(r, 1000 + Math.random() * 2000));
    const res = await shareOnce(account.token, account.cookie, postUrl);
    if (res.success) {
      console.log(green(`✅ SUCCESS ${i}/${shares} | ID: ${res.id}`)); 
      success++;
      account.shareCount++;
      account.lastShare = new Date().toISOString();
    } else {
      console.log(red(`❌ FAILED ${i}/${shares} | ${res.error}`));
    }
  }
 
  AccountManager.saveAccounts(accounts);
 
console.log(cyan('\n═════════════════════════════════════════════════════════════════════════'));
console.log(cyan('                     SINGLE SHARE COMPLETED!                     '));
console.log(cyan('═════════════════════════════════════════════════════════════════════════'));
console.log(green(`  SUCCESSFUL SHARES: \( {success}/ \){shares}`.padEnd(60)));
console.log(cyan(`  SUCCESS RATE:      ${((success/shares)*100).toFixed(1)}%`.padEnd(60)));
console.log(blue(`  ACCOUNT USED:      ${account.id}`.padEnd(60)));
console.log(yellow(`  POST URL:          ${postUrl.substring(0, 50)}...`.padEnd(60)));
console.log(cyan('═════════════════════════════════════════════════════════════════════════'));
console.log(cyan('  Thank you for using FB Auto Share v1.1 FAST EDITION!'));
console.log(cyan('═════════════════════════════════════════════════════════════════════════\n'));
}
 
async function showMenu() {
  console.log(magenta('\n╔════════════════════════════════════════════════════════════════════════════╗'));
  console.log(magenta('║                      🚀 FB AUTO SHARE v1.1 MAIN MENU 🚀                    ║'));
  console.log(magenta('╠════════════════════════════════════════════════════════════════════════════╣'));
 
  console.log(cyan('║  [1] 💫 Add New Account      │ [5] 🌪️ Mass Share (UP TO 4000 SHARES)        ║'));
  console.log(cyan('║  [2] 📋 List All Accounts    │ [6] 📊 Statistics                           ║'));
  console.log(cyan('║  [3] 🗑️  Remove Account       │ [7] 🔄 Toggle Status                        ║'));
  console.log(cyan('║  [4] ⚡ Single Share         │ [8] 📚 Help                                 ║'));
  console.log(cyan('║                              │ [9] 🔧 Settings                             ║'));
  console.log(cyan('║                              │ [0] 🚪 Exit                                 ║'));
 
  console.log(magenta('╠════════════════════════════════════════════════════════════════════════════╣'));
  console.log(yellow('║  ⚡ FAST EDITION - ULTRA FAST SHARING • 4000 SHARES PER ACCOUNT            ║'));
  console.log(blue('║  💖 Made by  by Jhames Martin - PH Edition 2025                      ║'));
  console.log(magenta('╚════════════════════════════════════════════════════════════════════════════╝'));
}
 
async function showStats() {
  const accounts = AccountManager.loadAccounts();
  if (accounts.length === 0) {
    console.log(red('\n╔══════════════════════════════════════════════════════════════╗'));
    console.log(red('║                  ❌ NO STATISTICS AVAILABLE ❌              ║'));
    console.log(red('╠══════════════════════════════════════════════════════════════╣'));
    console.log(yellow('║  💡 Add accounts first to see statistics                     ║'));
    console.log(red('╚══════════════════════════════════════════════════════════════╝'));
    return;
  }
 
  const totalShares = accounts.reduce((sum, acc) => sum + acc.shareCount, 0);
  const activeAccounts = accounts.filter(acc => acc.status === 'active').length;
  const totalAccounts = accounts.length;
  const totalSuccessRate = totalShares > 0 ? ((accounts.filter(acc => acc.shareCount > 0).length / totalAccounts) * 100).toFixed(1) : '0';
 
console.log(magenta('\n═════════════════════════════════════════════════════════════════════════'));
console.log(magenta('                       COMPREHENSIVE STATISTICS                       '));
console.log(magenta('═════════════════════════════════════════════════════════════════════════'));
console.log(cyan('  OVERVIEW'));
console.log(cyan('─────────────────────────────────────────────────────────────────────────'));
console.log(blue(`  Total Accounts:            ${totalAccounts}`.padEnd(60)));
console.log(green(`  Active Accounts:           ${activeAccounts}`.padEnd(60)));
console.log(red(`  Inactive Accounts:         ${totalAccounts - activeAccounts}`.padEnd(60)));
console.log(yellow(`  Total Shares:              ${totalShares}`.padEnd(60)));
console.log(magenta('═════════════════════════════════════════════════════════════════════════\n'));
 
if (totalShares > 0) {
  console.log(cyan(`  AVERAGE SHARES PER ACCOUNT: ${(totalShares / totalAccounts).toFixed(1)}`.padEnd(60)));
  console.log(magenta(`  OVERALL SUCCESS RATE:        ${totalSuccessRate}%`.padEnd(60)));
}
 
console.log(''); 
console.log(cyan('═════════════════════════════════════════════════════════════════════════'));
console.log(cyan('                       DETAILED PER-ACCOUNT BREAKDOWN                   '));
console.log(cyan('═════════════════════════════════════════════════════════════════════════'));
 
accounts.forEach((acc, i) => {
  const statusColor = acc.status === 'active' ? green('ACTIVE') : red('INACTIVE');
  const readiness   = acc.status === 'active' ? 'Ready   ' : 'Paused  ';
  const lastShare   = acc.lastShare ? new Date(acc.lastShare).toLocaleDateString() : 'Never   ';
  const addedDate   = acc.added.split('T')[0];
 
  console.log(cyan(`  \( {String(i + 1).padEnd(2)} │ ID: \){acc.id.substring(0, 10)}... │ \( {statusColor} │ Shares: \){String(acc.shareCount).padEnd(4)} │ Added: ${addedDate}`));
  console.log(cyan(`     └ Last Share: \( {lastShare.padEnd(12)} │ Status: \){readiness}`));
  console.log(''); 
});
 
console.log(cyan('═════════════════════════════════════════════════════════════════════════'));
console.log(yellow('  Tip: Keep accounts ACTIVE for maximum sharing power & speed!'));
console.log(cyan('═════════════════════════════════════════════════════════════════════════\n'));
}
async function showSettings() {
  console.log(magenta('\n🔧 SETTINGS & CONFIGURATION - FAST EDITION'));
  console.log(cyan('═'.repeat(50)));
  console.log('⚙️ Current Configuration:');
  console.log(`📁 Data File: ${ACCOUNTS_FILE}`);
  console.log(`📊 Auto-save: Enabled`);
  console.log(`🌐 API Version: v20.0`);
  console.log(`⚡ Fast Rate Limiting: 0-5 seconds`);
  console.log(`🎯 MAX Shares/Account: 4000 (ENFORCED)`);
  console.log(`🚀 Speed Mode: OPTIMIZED`);
  console.log(`📱 Termux Compatible: ✅`);
  console.log(cyan('\n⚡ Performance Optimizations:'));
  console.log('• Reduced delays for faster sharing');
  console.log('• Parallel processing for mass sharing');
  console.log('• Enhanced error handling');
  console.log('• Account limit enforcement');
  console.log(cyan('\n⚠️ Important Notes:'));
  console.log('• Fast mode may trigger rate limits faster');
  console.log('• Monitor account health regularly');
  console.log('• Keep account status updated');
  console.log('• Backup your accounts.json file regularly');
}
 
async function main() {
  while (true) {
    await showMenu();
    const choice = await ask(cyan('\n[+] Select option (0-9 or h for help): '));
 
    switch (choice.toLowerCase()) {
      case '1':
        await AccountManager.addAccount();
        break;
      case '2':
        AccountManager.listAccounts();
        break;
      case '3':
        await AccountManager.removeAccount();
        break;
      case '4':
        await singleShare();
        break;
      case '5':
        await massShare();
        break;
      case '6':
        await showStats();
        break;
      case '7':
        AccountManager.toggleAccountStatus();
        break;
      case '8':
      case 'h':
        showHelp();
        break;
      case '9':
        await showSettings();
        break;
      case '0':
      case 'exit':
        console.log(cyan('\n👋 Thank you for using FB Auto Share v1.1!'));
        console.log(magenta('💖 Made by  by Jhames Martin'));
        console.log(cyan('🌟 Termux Ready • PH Edition 2025'));
        console.log(yellow('🚀 Happy sharing! See you next time!'));
        rl.close();
        return;
      default:
        console.log(red('\n❌ Invalid option! Please select 0-9 or h for help.'));
    }
 
    await ask(cyan('\n[+] Press Enter to continue...'));
  }
}
 
function startMain() { 
  main().catch(e => { 
    console.log(red(`\n❌ Critical Error: ${e.message}`)); 
    console.log(yellow('💡 Try running with --debug for more details'));
    process.exit(1); 
  }); 
}
 
if (process.argv.includes('--help') || process.argv.includes('-h')) {
  showHelp();
  process.exit(0);
}
 
if (process.argv.includes('--version') || process.argv.includes('-v')) {
  console.log('FB Auto Share v1.1 - Multi Account Edition');
  console.log('Made by Jhames Martin - PH Edition 2025');
  process.exit(0);
}
 
printAnimatedBanner();
create new paste  /  syntax languages  /  archive  /  faq  /  tools  /  night mode  /  api  /  scraping api  /  news  /  pro
privacy statement  /  cookies policy  /  terms of service /  security disclosure  /  dmca  /  report abuse  /  contact

