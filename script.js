/* ═══════════════════════════════════════════════════════════
   portfolioHUB — script.js
   ═══════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  /* ── Sticky Header ── */
  const header = document.getElementById('header');
  const onScroll = () => {
    header.classList.toggle('scrolled', window.scrollY > 40);
  };
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ── Active Nav Link ── */
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.header__nav a');

  const observerNav = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        navLinks.forEach(link => {
          link.classList.toggle('active', link.getAttribute('href') === '#' + entry.target.id);
        });
      }
    });
  }, { rootMargin: '-40% 0px -55% 0px' });

  sections.forEach(s => observerNav.observe(s));

  /* ── Hamburger Menu ── */
  const hamburger = document.getElementById('hamburger');
  const nav = document.getElementById('nav');
  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('open');
    nav.classList.toggle('open');
  });
  // Close on link click
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      hamburger.classList.remove('open');
      nav.classList.remove('open');
    });
  });

  /* ── Scroll Reveal ── */
  const revealEls = document.querySelectorAll(
    '.perfil__grid, .curriculo__col, .curriculo__card, .project-card, .hab-area, .slides-embed, .contato__inner'
  );
  revealEls.forEach(el => el.classList.add('reveal'));

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        entry.target.style.transitionDelay = `${i * 0.06}s`;
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -60px 0px' });

  revealEls.forEach(el => revealObserver.observe(el));

  /* ── Animate Progress Bars on scroll ── */
  const bars = document.querySelectorAll('.hab-bar__fill, .lang-bar__fill');
  const barObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.animationPlayState = 'running';
        barObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });
  bars.forEach(b => barObserver.observe(b));

  /* ── Project Filter ── */
  const filterBtns = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const filter = btn.dataset.filter;
      filterBtns.forEach(b => b.classList.remove('filter-btn--active'));
      btn.classList.add('filter-btn--active');

      projectCards.forEach(card => {
        const show = filter === 'todos' || card.dataset.category === filter;
        card.classList.toggle('hidden', !show);
        // Animate entry
        if (show) {
          card.style.animation = 'none';
          card.offsetHeight; // reflow
          card.style.animation = 'fadeUp .4s ease both';
        }
      });
    });
  });

  /* ── Smooth counter for stats (optional enhancement) ── */
  function animateValue(el, start, end, duration) {
    const range = end - start;
    const startTime = performance.now();
    const update = (currentTime) => {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.floor(start + range * eased);
      if (progress < 1) requestAnimationFrame(update);
    };
    requestAnimationFrame(update);
  }

  /* ── Typed cursor effect on hero subtitle ── */
  const subtitleEl = document.querySelector('.hero__subtitle');
  if (subtitleEl) {
    const words = ['Desenvolvedor', 'Designer', 'Inovador', 'Criador'];
    let wordIndex = 0;
    let charIndex = 0;
    let deleting = false;
    let pause = false;

    function typeEffect() {
      if (pause) return;
      const current = words[wordIndex];
      if (deleting) {
        charIndex--;
      } else {
        charIndex++;
      }

      const parts = words.slice(0, words.length - 1)
        .filter((_, i) => i !== wordIndex);
      subtitleEl.textContent = current.slice(0, charIndex);

      let speed = deleting ? 60 : 110;

      if (!deleting && charIndex === current.length) {
        speed = 1800;
        deleting = true;
      } else if (deleting && charIndex === 0) {
        deleting = false;
        wordIndex = (wordIndex + 1) % words.length;
        speed = 300;
      }
      setTimeout(typeEffect, speed);
    }

    // Only activate if we have the element
    setTimeout(typeEffect, 1200);
  }

  /* ── Back to top on logo click ── */
  document.querySelector('.header__logo').addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

})();
