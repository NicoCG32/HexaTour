(function(){
  'use strict';
  const $$ = s => document.querySelectorAll(s);
  function goLugar(cat){
    const base = location.pathname.replace(/[^\/]+$/, '');
    location.href = window.HexaTour.withMode(base + 'lugar.html?cat=' + encodeURIComponent(cat));
  }
  document.addEventListener('DOMContentLoaded', ()=>{
    if(window.HexaTour.isDemo){
      document.querySelector('.sub').textContent = 'Elige una categoría para ver lugares e imágenes de ruta.';
    }
    $$('#categorias .btn-cat').forEach(btn=>{
      btn.addEventListener('click', ()=>goLugar(btn.dataset.cat), {passive:true});
    });
  });
})();
