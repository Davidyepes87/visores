const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const cat = JSON.parse(fs.readFileSync('repo/catalogo.json'));
  const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  for (const v of cat.visores) {
    const out = `repo/miniaturas/${v.id}.png`; if (fs.existsSync(out)) continue;
    const p = await b.newPage({ viewport: { width: 1280, height: 800 } });
    const t0 = Date.now();
    try { await p.goto('file:///home/claude/visores-trabajo/repo/' + v.vistas[0].url, { timeout: 90000, waitUntil: 'load' }); } catch (e) { console.log(v.id, 'goto', e.message.slice(0, 80)); }
    await p.waitForTimeout(v.vistas[0].mb > 30 ? 25000 : 14000);
    await p.screenshot({ path: out }).catch(e => console.log(v.id, 'shot', e.message));
    console.log(v.id, ((Date.now() - t0) / 1000).toFixed(0) + 's');
    await p.close();
  }
  await b.close();
})();
