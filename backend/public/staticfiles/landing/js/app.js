/* MrExchange Landing Page — interactions, i18n and animations.
 *
 * Layers (progressive enhancement):
 *  1. Core (always): i18n, language switcher, FAQ, mobile menu, smooth scroll, tabs.
 *  2. GSAP (if loaded): scroll reveals, counters, parallax, hero intro.
 *  3. Canvas (always, respects reduced motion): hero particle network + product flow.
 */
(function () {
    'use strict';

    var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    var REDUCED = prefersReducedMotion.matches;

    /* ════════════════════════ 1. i18n engine ════════════════════════ */

    var I18N = window.MrX_I18N || {};
    var RTL_LANGS = { fa: true, ar: true };
    var LANG_KEY = 'mrx-lang';

    function detectLang() {
        // ?lang=en|fa|tr|ar|de — allows shareable links in a specific language.
        var urlLang = new URLSearchParams(window.location.search).get('lang');
        if (urlLang && I18N[urlLang]) return urlLang;
        var stored = null;
        try { stored = localStorage.getItem(LANG_KEY); } catch (e) { /* private mode */ }
        if (stored && I18N[stored]) return stored;
        var nav = (navigator.language || 'fa').toLowerCase();
        var map = { fa: 'fa', ar: 'ar', tr: 'tr', de: 'de' };
        if (map[nav]) return map[nav];
        if (nav.indexOf('ar') === 0) return 'ar';
        if (nav.indexOf('tr') === 0) return 'tr';
        if (nav.indexOf('de') === 0) return 'de';
        return 'fa'; // default — Persian
    }

    var currentLang = detectLang();

    function t(key) {
        var lang = I18N[currentLang] || {};
        var fallback = I18N.fa || {};
        return lang[key] !== undefined ? lang[key] : (fallback[key] !== undefined ? fallback[key] : '');
    }

    function applyTranslations() {
        document.documentElement.lang = currentLang;
        document.documentElement.dir = RTL_LANGS[currentLang] ? 'rtl' : 'ltr';

        // data-i18n → textContent
        document.querySelectorAll('[data-i18n]').forEach(function (el) {
            var key = el.getAttribute('data-i18n');
            var val = t(key);
            if (val) el.textContent = val;
        });

        // data-i18n-html → innerHTML (FAQ answers, feature list items with <strong>, etc.)
        document.querySelectorAll('[data-i18n-html]').forEach(function (el) {
            var key = el.getAttribute('data-i18n-html');
            var val = t(key);
            if (val) el.innerHTML = val;
        });

        // data-i18n-ph → placeholder attribute (contact form inputs)
        document.querySelectorAll('[data-i18n-ph]').forEach(function (el) {
            var key = el.getAttribute('data-i18n-ph');
            var val = t(key);
            if (val) el.setAttribute('placeholder', val);
        });

        // language switcher: mark the active option (the generic [data-i18n] pass
        // already set the button label to the native name of the current language)
        document.querySelectorAll('.lang-menu [data-lang]').forEach(function (btn) {
            var isSel = btn.getAttribute('data-lang') === currentLang;
            btn.setAttribute('aria-selected', isSel ? 'true' : 'false');
        });

        // document title stays Persian for SEO; body is translated at runtime.
        document.title = t('hero.title1') + ' | MrExchange';

        // Redraw canvas labels (product flow) in the new language.
        if (window.MrXFlow && typeof window.MrXFlow.redraw === 'function') window.MrXFlow.redraw();

        // Re-fire reveal so ScrollTrigger measures fresh text sizes.
        if (window.ScrollTrigger) window.ScrollTrigger.refresh();
    }

    function setLang(lang) {
        if (!I18N[lang]) return;
        currentLang = lang;
        try { localStorage.setItem(LANG_KEY, lang); } catch (e) { /* ignore */ }
        applyTranslations();
    }

    /* Language switcher UI */
    var langBtn = document.getElementById('langBtn');
    var langMenu = document.querySelector('.lang-menu');
    if (langBtn && langMenu) {
        langBtn.addEventListener('click', function (e) {
            e.stopPropagation();
            var open = langMenu.classList.toggle('open');
            langBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
        });
        document.addEventListener('click', function (e) {
            if (!langMenu.contains(e.target)) {
                langMenu.classList.remove('open');
                langBtn.setAttribute('aria-expanded', 'false');
            }
        });
        langMenu.addEventListener('click', function (e) {
            var btn = e.target.closest('[data-lang]');
            if (btn) {
                setLang(btn.getAttribute('data-lang'));
                langMenu.classList.remove('open');
                langBtn.setAttribute('aria-expanded', 'false');
            }
        });
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') {
                langMenu.classList.remove('open');
                langBtn.setAttribute('aria-expanded', 'false');
            }
        });
    }

    /* ════════════════════════ 2. Core UI (no dependencies) ════════════════════════ */

    document.addEventListener('DOMContentLoaded', function () {
        applyTranslations();

        /* FAQ accordion — one open at a time. */
        var faqs = document.querySelectorAll('.faq-item');
        faqs.forEach(function (faq) {
            var question = faq.querySelector('.faq-question');
            if (!question) return;
            question.setAttribute('role', 'button');
            question.setAttribute('tabindex', '0');
            question.setAttribute('aria-expanded', 'false');

            var toggle = function () {
                var wasActive = faq.classList.contains('active');
                faqs.forEach(function (f) {
                    f.classList.remove('active');
                    var q = f.querySelector('.faq-question');
                    if (q) q.setAttribute('aria-expanded', 'false');
                });
                if (!wasActive) {
                    faq.classList.add('active');
                    question.setAttribute('aria-expanded', 'true');
                }
            };
            question.addEventListener('click', toggle);
            question.addEventListener('keydown', function (e) {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    toggle();
                }
            });
        });

        /* Mobile menu */
        var menuToggle = document.getElementById('menuToggle');
        var navLinks = document.getElementById('navLinks');
        if (menuToggle && navLinks) {
            var setMenu = function (open) {
                navLinks.classList.toggle('active', open);
                menuToggle.classList.toggle('active', open);
                menuToggle.setAttribute('aria-expanded', String(open));
            };
            menuToggle.addEventListener('click', function () {
                setMenu(!menuToggle.classList.contains('active'));
            });
            navLinks.querySelectorAll('a').forEach(function (link) {
                link.addEventListener('click', function () { setMenu(false); });
            });
            document.addEventListener('keydown', function (e) {
                if (e.key === 'Escape') setMenu(false);
            });
        }

        /* Smooth scroll (guarded against missing anchors) */
        document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
            anchor.addEventListener('click', function (e) {
                var targetId = this.getAttribute('href');
                if (!targetId || targetId === '#') return;
                var target = null;
                try { target = document.querySelector(targetId); } catch (err) { return; }
                if (!target) return;
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth' });
            });
        });

        /* Showcase tabs */
        var tabs = document.querySelectorAll('.showcase-tab');
        var panels = document.querySelectorAll('.showcase-panel');
        tabs.forEach(function (tab) {
            tab.addEventListener('click', function () {
                var name = tab.getAttribute('data-tab');
                tabs.forEach(function (b) {
                    b.classList.toggle('active', b === tab);
                    b.setAttribute('aria-selected', b === tab ? 'true' : 'false');
                });
                panels.forEach(function (p) {
                    var active = p.getAttribute('data-panel') === name;
                    p.classList.toggle('active', active);
                });
            });
        });

        /* Ticker: duplicate content for a seamless loop */
        var track = document.getElementById('tickerTrack');
        if (track) {
            track.innerHTML += track.innerHTML;
        }
        var ecoTrack = document.getElementById('ecoTrack');
        if (ecoTrack) {
            ecoTrack.innerHTML += ecoTrack.innerHTML;
        }

        /* Reading progress bar */
        var progressBar = document.getElementById('progressBar');
        var onScroll = function () {
            if (!progressBar) return;
            var h = document.documentElement;
            var max = h.scrollHeight - h.clientHeight;
            var pct = max > 0 ? (h.scrollTop || document.body.scrollTop) / max : 0;
            progressBar.style.transform = 'scaleX(' + pct + ')';
        };
        window.addEventListener('scroll', onScroll, { passive: true });
        onScroll();

        /* Live price jitter on hero dashboard — subtle, for the “live” feel */
        var livePrices = document.querySelectorAll('.live-price');
        if (livePrices.length && !REDUCED) {
            setInterval(function () {
                livePrices.forEach(function (el) {
                    var base = parseFloat(el.getAttribute('data-base'));
                    if (!base) return;
                    var delta = (Math.random() - 0.5) * 0.004;
                    var next = base + delta;
                    el.textContent = '\u00A3 ' + next.toFixed(3);
                    var parent = el.closest('.c-price');
                    if (parent) {
                        parent.classList.remove('price-up', 'price-down');
                        parent.classList.add(delta >= 0 ? 'price-up' : 'price-down');
                    }
                });
            }, 2200);
        }

        initHeroCanvas();
        /* The product-flow canvas (window.MrXFlow) self-initialises at parse time. */

        /* ════════════════ 3. GSAP layer (progressive) ════════════════ */
        if (window.gsap && window.ScrollTrigger && !REDUCED) {
            gsap.registerPlugin(ScrollTrigger);

            /* Hero intro timeline */
            gsap.timeline({ defaults: { ease: 'power3.out' } })
                .from('.hero .hero-badge', { y: 24, autoAlpha: 0, duration: 0.7 }, 0.15)
                .from('.hero h1', { y: 40, autoAlpha: 0, duration: 0.8 }, 0.25)
                .from('.hero-content p', { y: 30, autoAlpha: 0, duration: 0.7 }, 0.4)
                .from('.hero-buttons .btn', { y: 20, autoAlpha: 0, duration: 0.5, stagger: 0.12 }, 0.55)
                .from('.feature-badges .badge', { y: 16, autoAlpha: 0, duration: 0.4, stagger: 0.08 }, 0.7)
                .from('.hero-visual', { x: 60, autoAlpha: 0, duration: 0.9, ease: 'power2.out' }, 0.45)
                .from('.float-card', { scale: 0, autoAlpha: 0, duration: 0.5, stagger: 0.12, ease: 'back.out(2)' }, 0.9)
                .from('.scroll-indicator', { autoAlpha: 0, duration: 0.5 }, 1.3);

            /* Scroll reveals: elements marked .reveal fade+rise as they enter.
               Hero elements are excluded — they have their own intro timeline. */
            gsap.utils.toArray('.reveal').forEach(function (el) {
                if (el.closest('.hero')) return;
                gsap.fromTo(el,
                    { autoAlpha: 0, y: 48 },
                    {
                        autoAlpha: 1, y: 0, duration: 0.8, ease: 'power2.out',
                        scrollTrigger: { trigger: el, start: 'top 85%', once: true }
                    }
                );
            });

            /* Counters */
            gsap.utils.toArray('.counter').forEach(function (el) {
                var target = parseInt(el.getAttribute('data-target'), 10) || 0;
                var obj = { v: 0 };
                gsap.to(obj, {
                    v: target, duration: 1.8, ease: 'power2.out',
                    scrollTrigger: { trigger: el, start: 'top 88%', once: true },
                    onUpdate: function () { el.textContent = Math.round(obj.v); }
                });
            });

            /* Parallax on hero orbs / decorative layer */
            gsap.to('.bg-orbs', {
                yPercent: 18, ease: 'none',
                scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: 1 }
            });

            /* Dashboard mockup subtle float */
            gsap.to('.hero-visual .mock-dashboard', {
                y: -14, duration: 3, yoyo: true, repeat: -1, ease: 'sine.inOut'
            });

            /* Navbar shrink on scroll */
            ScrollTrigger.create({
                start: 80,
                onUpdate: function (self) {
                    document.querySelector('.navbar').classList.toggle('scrolled', self.scroll() > 80);
                }
            });
        } else {
            /* No GSAP / reduced motion: make everything visible immediately */
            document.querySelectorAll('.reveal').forEach(function (el) {
                el.style.opacity = '1';
                el.style.transform = 'none';
            });
        }
    });

    /* ════════════════════════ Hero particle network canvas ════════════════════════ */

    function initHeroCanvas() {
        var canvas = document.getElementById('heroCanvas');
        if (!canvas) return;
        var ctx = canvas.getContext('2d');
        var W, H, particles = [];
        var DPR = Math.min(window.devicePixelRatio || 1, 2);

        function resize() {
            W = canvas.offsetWidth;
            H = canvas.offsetHeight;
            canvas.width = W * DPR;
            canvas.height = H * DPR;
            canvas.style.width = W + 'px';
            canvas.style.height = H + 'px';
            ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
            var count = Math.min(70, Math.floor((W * H) / 22000));
            particles = [];
            for (var i = 0; i < count; i++) {
                particles.push({
                    x: Math.random() * W,
                    y: Math.random() * H,
                    vx: (Math.random() - 0.5) * 0.35,
                    vy: (Math.random() - 0.5) * 0.35,
                    r: Math.random() * 1.8 + 0.6,
                    c: Math.random() > 0.75 ? 'rgba(21,153,78,' : 'rgba(59,130,246,'
                });
            }
        }

        function draw() {
            ctx.clearRect(0, 0, W, H);
            var i, j;
            // links
            for (i = 0; i < particles.length; i++) {
                for (j = i + 1; j < particles.length; j++) {
                    var dx = particles[i].x - particles[j].x;
                    var dy = particles[i].y - particles[j].y;
                    var d2 = dx * dx + dy * dy;
                    if (d2 < 140 * 140) {
                        var a = (1 - Math.sqrt(d2) / 140) * 0.22;
                        ctx.strokeStyle = 'rgba(120,180,150,' + a.toFixed(3) + ')';
                        ctx.lineWidth = 1;
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.stroke();
                    }
                }
            }
            // dots
            for (i = 0; i < particles.length; i++) {
                var p = particles[i];
                p.x += p.vx; p.y += p.vy;
                if (p.x < -10) p.x = W + 10; if (p.x > W + 10) p.x = -10;
                if (p.y < -10) p.y = H + 10; if (p.y > H + 10) p.y = -10;
                ctx.fillStyle = p.c + '0.55)';
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                ctx.fill();
            }
            requestAnimationFrame(draw);
        }

        resize();
        window.addEventListener('resize', resize);
        if (REDUCED) return; // static dots only
        draw();
    }

    /* ════════════════════════ Product flow canvas (the “cool” one) ════════════════════════ */

    /* A central panel node pushes glowing particles along bezier paths to 5 channels. */
    window.MrXFlow = (function () {
        var canvas = document.getElementById('flowCanvas');
        if (!canvas) return { redraw: function () {} };

        var ctx = canvas.getContext('2d');
        var W, H, DPR = Math.min(window.devicePixelRatio || 1, 2);
        var nodes = [];      // {x, y, r, label, color, icon}
        var particles = [];
        var running = false;
        var inView = false;

        var NODE_KEYS = ['panel', 'telegram', 'instagram', 'website', 'tv', 'bot'];
        var COLORS = {
            telegram: '#2AABEE',
            instagram: '#E1306C',
            website: '#3B82F6',
            tv: '#F59E0B',
            bot: '#8B5CF6'
        };
        var ICONS = { telegram: '\u2708\uFE0F', instagram: '\uD83D\uDCF8', website: '\uD83C\uDF10', tv: '\uD83D\uDCFA', bot: '\uD83E\uDD16', panel: '\uD83D\uDCBB' };

        function lang() {
            return document.documentElement.lang || 'fa';
        }
        function labelFor(key) {
            var dict = (window.MrX_I18N && window.MrX_I18N[lang()]) || {};
            var fallback = (window.MrX_I18N && window.MrX_I18N.fa) || {};
            var v = dict['pipeline.node.' + key];
            if (v === undefined) v = fallback['pipeline.node.' + key];
            return v || key;
        }

        function layout() {
            var pad = 60;
            nodes = [];
            var cx = W / 2, cy = H / 2;
            var rx = Math.min(W / 2 - pad, 320);
            var ry = Math.min(H / 2 - pad, 190);
            var targets = [
                { key: 'telegram', angle: -Math.PI / 2 },
                { key: 'instagram', angle: -Math.PI / 2 + Math.PI / 2.4 },
                { key: 'website', angle: -Math.PI / 2 + Math.PI / 1.2 },
                { key: 'tv', angle: -Math.PI / 2 - Math.PI / 2.4 },
                { key: 'bot', angle: -Math.PI / 2 - Math.PI / 1.2 }
            ];
            targets.forEach(function (tgt, idx) {
                // Spread evenly around the ellipse
                var a = -Math.PI / 2 + (idx / 5) * Math.PI * 2;
                nodes.push({
                    key: tgt.key,
                    x: cx + Math.cos(a) * rx,
                    y: cy + Math.sin(a) * ry * 0.9,
                    r: 34,
                    color: COLORS[tgt.key] || '#3B82F6',
                    icon: ICONS[tgt.key]
                });
            });
        }

        function resize() {
            W = canvas.offsetWidth;
            H = canvas.offsetHeight;
            canvas.width = W * DPR;
            canvas.height = H * DPR;
            canvas.style.width = W + 'px';
            canvas.style.height = H + 'px';
            ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
            layout();
        }

        function spawn() {
            var target = nodes[Math.floor(Math.random() * nodes.length)];
            var start = { x: W / 2, y: H / 2 };
            var ctrl1 = { x: (start.x + target.x) / 2 + (Math.random() - 0.5) * 120, y: (start.y + target.y) / 2 + (Math.random() - 0.5) * 120 };
            var speed = 0.02 + Math.random() * 0.02;
            particles.push({
                t: 0, speed: speed, target: target, start: start, ctrl1: ctrl1,
                r: 2 + Math.random() * 2,
                color: target.color
            });
        }

        function bezier(p, t) {
            var u = 1 - t;
            return {
                x: u * u * p.start.x + 2 * u * t * p.ctrl1.x + t * t * p.target.x,
                y: u * u * p.start.y + 2 * u * t * p.ctrl1.y + t * t * p.target.y
            };
        }

        function drawStatic() {
            ctx.clearRect(0, 0, W, H);
            if (nodes.length < 2) return;

            // connection lines (dashed, faint)
            nodes.forEach(function (n) {
                if (n.key === 'panel') return;
                ctx.save();
                ctx.setLineDash([5, 6]);
                ctx.strokeStyle = n.color;
                ctx.globalAlpha = 0.35;
                ctx.lineWidth = 1.5;
                ctx.beginPath();
                ctx.moveTo(W / 2, H / 2);
                ctx.quadraticCurveTo((W / 2 + n.x) / 2, (H / 2 + n.y) / 2 - 30, n.x, n.y);
                ctx.stroke();
                ctx.restore();
            });

            // center node
            var cx = W / 2, cy = H / 2;
            var grad = ctx.createRadialGradient(cx, cy, 5, cx, cy, 70);
            grad.addColorStop(0, 'rgba(21,153,78,0.5)');
            grad.addColorStop(1, 'rgba(21,153,78,0)');
            ctx.fillStyle = grad;
            ctx.beginPath();
            ctx.arc(cx, cy, 70, 0, Math.PI * 2);
            ctx.fill();

            ctx.fillStyle = 'rgba(21,153,78,0.15)';
            ctx.strokeStyle = 'rgba(21,153,78,0.8)';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.arc(cx, cy, 42, 0, Math.PI * 2);
            ctx.fill();
            ctx.stroke();

            ctx.font = '24px sans-serif';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText('\uD83D\uDCBB', cx, cy);

            // channel nodes
            nodes.forEach(function (n) {
                ctx.fillStyle = 'rgba(13,16,22,0.9)';
                ctx.strokeStyle = n.color;
                ctx.lineWidth = 2;
                ctx.beginPath();
                ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
                ctx.fill();
                ctx.stroke();

                ctx.fillStyle = n.color;
                ctx.globalAlpha = 0.25;
                ctx.beginPath();
                ctx.arc(n.x, n.y, n.r + 8 + Math.sin(Date.now() / 700 + n.x) * 2, 0, Math.PI * 2);
                ctx.fill();
                ctx.globalAlpha = 1;

                ctx.font = '18px sans-serif';
                ctx.fillText(n.icon, n.x, n.y);

                ctx.font = '600 13px Vazirmatn, sans-serif';
                ctx.fillStyle = 'rgba(243,244,246,0.92)';
                ctx.fillText(labelFor(n.key), n.x, n.y + n.r + 18);
            });

            // center label
            ctx.font = '700 14px Vazirmatn, sans-serif';
            ctx.fillStyle = 'rgba(243,244,246,0.95)';
            ctx.fillText(labelFor('panel'), cx, cy + 66);
        }

        var last = 0;
        function frame(ts) {
            if (!running) return;
            var dt = Math.min((ts - last) / 16.667, 3) || 1;
            last = ts;

            if (Math.random() < 0.5 * dt) spawn();
            if (particles.length > 60) particles.splice(0, particles.length - 60);

            drawStatic();
            ctx.save();
            particles.forEach(function (p) {
                p.t += p.speed * dt;
                var pos = bezier(p, Math.min(p.t, 1));
                var alpha = p.t > 0.92 ? (1 - p.t) * 12 : 1;
                ctx.globalAlpha = Math.max(alpha, 0);
                ctx.fillStyle = p.color;
                ctx.shadowColor = p.color;
                ctx.shadowBlur = 8;
                ctx.beginPath();
                ctx.arc(pos.x, pos.y, p.r, 0, Math.PI * 2);
                ctx.fill();
            });
            ctx.restore();

            particles = particles.filter(function (p) { return p.t < 1; });
            requestAnimationFrame(frame);
        }

        function start() {
            if (running) return;
            running = true;
            last = performance.now();
            requestAnimationFrame(frame);
        }
        function stop() {
            running = false;
        }

        resize();
        window.addEventListener('resize', resize);

        // IntersectionObserver: animate only while visible.
        if ('IntersectionObserver' in window) {
            new IntersectionObserver(function (entries) {
                entries.forEach(function (entry) {
                    inView = entry.isIntersecting;
                    if (inView && !REDUCED) start();
                    else stop();
                });
            }, { threshold: 0.15 }).observe(canvas);
        } else if (!REDUCED) {
            start();
        }

        // Always render a static frame (labels translated correctly).
        function drawOnce() { drawStatic(); }
        window.addEventListener('resize', drawOnce);
        drawOnce();

        return { redraw: function () { drawOnce(); } };
    })();

})();
