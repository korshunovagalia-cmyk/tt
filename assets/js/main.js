/* Tint & Sun — site interactions */
(function () {
  'use strict';

  /* ---- mobile drawer ---- */
  var burger = document.querySelector('.nav__burger');
  if (burger) {
    burger.addEventListener('click', function () {
      var open = document.body.classList.toggle('menu-open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.style.overflow = open ? 'hidden' : '';
    });
  }
  document.querySelectorAll('.drawer a').forEach(function (a) {
    a.addEventListener('click', function () {
      document.body.classList.remove('menu-open');
      document.body.style.overflow = '';
      if (burger) burger.setAttribute('aria-expanded', 'false');
    });
  });

  /* ---- accordion ---- */
  document.querySelectorAll('.acc__btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.acc__item');
      var panel = item.querySelector('.acc__panel');
      var inner = panel.firstElementChild;
      var open = item.classList.contains('is-open');

      if (open) {
        panel.style.height = inner.offsetHeight + 'px';
        requestAnimationFrame(function () { panel.style.height = '0px'; });
        item.classList.remove('is-open');
        btn.setAttribute('aria-expanded', 'false');
      } else {
        panel.style.height = inner.offsetHeight + 'px';
        item.classList.add('is-open');
        btn.setAttribute('aria-expanded', 'true');
        panel.addEventListener('transitionend', function once() {
          panel.style.height = 'auto';
          panel.removeEventListener('transitionend', once);
        });
      }
    });
  });

  /* ---- scroll reveal ---- */
  var targets = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && targets.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.style.transitionDelay = (e.target.dataset.delay || 0) + 'ms';
          e.target.classList.add('is-in');
          io.unobserve(e.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    targets.forEach(function (t) { io.observe(t); });
  } else {
    targets.forEach(function (t) { t.classList.add('is-in'); });
  }

  /* ---- contact form (front-end only) ---- */
  var form = document.querySelector('.form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = form.querySelector('.form__ok');
      if (ok) ok.classList.add('is-visible');
      form.reset();
    });
  }
})();
