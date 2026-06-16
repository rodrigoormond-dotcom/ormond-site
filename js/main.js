/* ================================================
   ORMOND STUDIO — Main JavaScript
   ================================================ */

// ---- NAV ----
const nav = document.getElementById('nav');
const burger = document.getElementById('nav-burger');
const mobileMenu = document.getElementById('mobile-menu');
const mobileClose = document.getElementById('mobile-close');

// Transparent nav on hero
function updateNav() {
  if (!nav) return;
  const hasHero = document.getElementById('hero');
  if (hasHero && window.scrollY < window.innerHeight * 0.5) {
    nav.classList.add('transparent');
  } else {
    nav.classList.remove('transparent');
  }
}
window.addEventListener('scroll', updateNav, { passive: true });
updateNav();

if (burger) {
  burger.addEventListener('click', () => mobileMenu.classList.add('open'));
}
if (mobileClose) {
  mobileClose.addEventListener('click', () => mobileMenu.classList.remove('open'));
}

// Active nav link
const currentPath = window.location.pathname;
document.querySelectorAll('.nav-links a, #mobile-menu a').forEach(a => {
  if (a.getAttribute('href') === currentPath ||
      (currentPath.includes(a.getAttribute('href')) && a.getAttribute('href') !== '/')) {
    a.classList.add('active');
  }
});

// ---- HERO SLIDESHOW ----
(function() {
  const slides = document.querySelectorAll('.hero-slide');
  const dots = document.querySelectorAll('.hero-dot');
  if (!slides.length) return;

  let current = 0;
  let timer;

  function showSlide(n) {
    slides[current].classList.remove('active');
    if (dots[current]) dots[current].classList.remove('active');
    current = (n + slides.length) % slides.length;
    slides[current].classList.add('active');
    if (dots[current]) dots[current].classList.add('active');
  }

  function next() { showSlide(current + 1); }

  function start() {
    timer = setInterval(next, 5000);
  }

  showSlide(0);
  start();

  dots.forEach((dot, i) => {
    dot.addEventListener('click', () => {
      clearInterval(timer);
      showSlide(i);
      start();
    });
  });
})();

// ---- LIGHTBOX ----
const lightbox = document.getElementById('lightbox');
const lbImg = document.getElementById('lightbox-img');
const lbCaption = document.getElementById('lightbox-caption');
let lbItems = [];
let lbIndex = 0;

function openLightbox(items, index) {
  lbItems = items;
  lbIndex = index;
  showLbItem();
  lightbox.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  lightbox.classList.remove('open');
  document.body.style.overflow = '';
}

function showLbItem() {
  if (!lbItems[lbIndex]) return;
  const { src, caption } = lbItems[lbIndex];
  lbImg.style.opacity = '0';
  setTimeout(() => {
    lbImg.src = src;
    if (lbCaption) lbCaption.textContent = caption || '';
    lbImg.style.opacity = '1';
    lbImg.style.transition = 'opacity 0.3s ease';
  }, 150);
}

function lbPrev() {
  lbIndex = (lbIndex - 1 + lbItems.length) % lbItems.length;
  showLbItem();
}

function lbNext() {
  lbIndex = (lbIndex + 1) % lbItems.length;
  showLbItem();
}

if (lightbox) {
  document.getElementById('lightbox-close')?.addEventListener('click', closeLightbox);
  document.getElementById('lightbox-prev')?.addEventListener('click', lbPrev);
  document.getElementById('lightbox-next')?.addEventListener('click', lbNext);
  lightbox.addEventListener('click', e => { if (e.target === lightbox) closeLightbox(); });
  document.addEventListener('keydown', e => {
    if (!lightbox.classList.contains('open')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') lbPrev();
    if (e.key === 'ArrowRight') lbNext();
  });
}

// Init masonry lightbox
function initMasonryLightbox() {
  const items = document.querySelectorAll('.masonry-item');
  const lbData = Array.from(items).map(item => ({
    src: item.querySelector('img')?.src || '',
    caption: item.dataset.caption || ''
  }));

  items.forEach((item, i) => {
    item.addEventListener('click', () => openLightbox(lbData, i));
  });
}
initMasonryLightbox();

// ---- VIDEO CATEGORY FILTER ----
function initVideoFilter() {
  const btns = document.querySelectorAll('.video-cat-btn');
  const sections = document.querySelectorAll('.video-section[data-cat]');
  if (!btns.length) return;

  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      const cat = btn.dataset.cat;
      btns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      sections.forEach(s => {
        if (cat === 'all' || s.dataset.cat === cat) {
          s.style.display = '';
        } else {
          s.style.display = 'none';
        }
      });
    });
  });
}
initVideoFilter();

// ---- FADE IN on scroll ----
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      observer.unobserve(e.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

// ---- GALLERY VIEW TOGGLE (grid / masonry) ----
function initViewToggle() {
  const btnGrid = document.getElementById('btn-grid');
  const btnMasonry = document.getElementById('btn-masonry');
  const gallery = document.querySelector('.masonry-grid');
  if (!btnGrid || !btnMasonry || !gallery) return;

  btnGrid.addEventListener('click', () => {
    gallery.style.columns = '4';
    gallery.style.columnGap = '3px';
    btnGrid.classList.add('active');
    btnMasonry.classList.remove('active');
  });

  btnMasonry.addEventListener('click', () => {
    gallery.style.columns = '3';
    btnMasonry.classList.add('active');
    btnGrid.classList.remove('active');
  });
}
initViewToggle();

// ---- BLOG: Render posts from JSON ----
async function loadBlogPosts() {
  const container = document.getElementById('blog-posts');
  if (!container) return;

  try {
    const res = await fetch('/blog/posts.json');
    if (!res.ok) return;
    const posts = await res.json();

    container.innerHTML = posts.map(post => `
      <article class="blog-card fade-in">
        ${post.image
          ? `<img class="blog-card-img" src="${post.image}" alt="${post.title}" loading="lazy">`
          : `<div class="blog-card-img-placeholder">📷</div>`}
        <div class="blog-card-body">
          <div class="blog-card-cat">${post.category || 'Blog'}</div>
          <h2 class="blog-card-title">${post.title}</h2>
          <p class="blog-card-excerpt">${post.excerpt || ''}</p>
          <div class="blog-card-meta">
            <time>${formatDate(post.date)}</time>
          </div>
          <a href="/blog/${post.slug}.html" class="blog-read-link">Ler mais →</a>
        </div>
      </article>
    `).join('');

    // Re-observe new elements
    document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
  } catch (e) {
    container.innerHTML = '<p style="color:var(--grey);text-align:center;padding:40px">Carregando posts...</p>';
  }
}

function formatDate(str) {
  if (!str) return '';
  const d = new Date(str);
  return d.toLocaleDateString('pt-BR', { day: '2-digit', month: 'long', year: 'numeric' });
}

loadBlogPosts();

// ---- Lazy load images ----
document.querySelectorAll('img[data-src]').forEach(img => {
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        img.src = img.dataset.src;
        img.removeAttribute('data-src');
        io.unobserve(img);
      }
    });
  });
  io.observe(img);
});
