(function(){
  'use strict';
  const $$ = s => document.querySelectorAll(s);
  function goLugar(cat){
    const base = location.pathname.replace(/[^\/]+$/, '');
    location.href = base + 'lugar.html?cat=' + encodeURIComponent(cat);
  }
  document.addEventListener('DOMContentLoaded', ()=>{
    $$('#categorias .btn-cat').forEach(btn=>{
      btn.addEventListener('click', ()=>goLugar(btn.dataset.cat), {passive:true});
    });
  });
})();
