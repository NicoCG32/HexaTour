(function(){
  'use strict';
  if(window.HexaTour.isDemo){
    document.querySelector('.card h1').textContent = 'Explorar HexaTour';
    document.querySelector('.card p').textContent = 'Abre el portal de demostración sin hardware.';
  }
  function go(){
    location.href = window.HexaTour.withMode(window.HexaTour.siteUrl('visitor/'));
  }
  const btn = document.getElementById('go');
  if(btn) btn.onclick = go;
  setTimeout(go, 2000);
})();
