(() => {
  const lessons = [...document.querySelectorAll('.lesson')];
  const search = document.querySelector('#search');
  const status = document.querySelector('#search-status');
  const tocLinks = [...document.querySelectorAll('[data-section-link]')];
  let savedOpen = null;
  document.querySelector('.toolbar').hidden = false;
  status.hidden = false;

  function filter() {
    const query = search.value.trim().toLocaleLowerCase();
    if (query && !savedOpen) savedOpen = new Map(lessons.map(el => [el, el.open]));
    let count = 0;
    for (const lesson of lessons) {
      const matches = !query || lesson.textContent.toLocaleLowerCase().includes(query);
      lesson.hidden = !matches;
      if (query && matches) lesson.open = true;
      if (!query && savedOpen) lesson.open = savedOpen.get(lesson);
      if (matches) count++;
      for (const link of tocLinks.filter(link => link.hash === '#' + lesson.id)) {
        link.closest('li').hidden = !matches;
      }
    }
    if (!query) savedOpen = null;
    status.textContent = query ? `${count} of ${lessons.length} sections match “${search.value.trim()}”.` : `${lessons.length} sections · Open a section to study · Double-click a formula to copy`;
    document.querySelector('#no-results').hidden = count !== 0;
  }
  search.addEventListener('input', filter);
  document.querySelector('#expand').addEventListener('click', () => {
    lessons.filter(el => !el.hidden).forEach(el => { el.open = true; });
  });
  document.querySelector('#collapse').addEventListener('click', () => {
    lessons.filter(el => !el.hidden).forEach(el => { el.open = false; });
  });
  document.querySelector('#print').addEventListener('click', () => window.print());

  function revealHash() {
    const id = decodeURIComponent(location.hash.slice(1));
    const target = document.getElementById(id);
    if (!target) return;
    if (search.value) { search.value = ''; filter(); }
    if (target.matches('.lesson')) target.open = true;
    const parent = target.closest('.lesson');
    if (parent) parent.open = true;
    tocLinks.forEach(link => {
      if (link.hash === '#' + id) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
    requestAnimationFrame(() => target.scrollIntoView({block:'start'}));
  }
  window.addEventListener('hashchange', revealHash);
  // Clicking the same fragment again must also reopen a collapsed section.
  tocLinks.forEach(link => link.addEventListener('click', () => {
    if (link.hash === location.hash) revealHash();
    const mobile = link.closest('.mobile-toc');
    if (mobile) mobile.open = false;
  }));
  let printState;
  window.addEventListener('beforeprint', () => {
    if (printState) return;
    printState = [...document.querySelectorAll('details')].map(el => [el, el.open, el.hidden]);
    for (const [el] of printState) { el.open = true; el.hidden = false; }
  });
  window.addEventListener('afterprint', () => {
    if (!printState) return;
    for (const [el, open, hidden] of printState) { el.open = open; el.hidden = hidden; }
    printState = null;
  });

  let copyTimer;
  document.addEventListener('dblclick', async event => {
    const code = event.target.closest('code');
    if (!code) return;
    const notice = document.querySelector('#copy-status');
    try {
      if (navigator.clipboard && window.isSecureContext) await navigator.clipboard.writeText(code.textContent);
      else {
        const area = document.createElement('textarea');
        area.value = code.textContent;
        area.style.position = 'fixed'; area.style.opacity = '0';
        document.body.append(area); area.select();
        const copied = document.execCommand('copy');
        area.remove();
        if (!copied) throw new Error('Copy unavailable');
      }
      notice.textContent = 'Formula copied';
    } catch { notice.textContent = 'Select the formula and use your browser’s Copy command.'; }
    notice.hidden = false;
    clearTimeout(copyTimer);
    copyTimer = setTimeout(() => { notice.hidden = true; }, 2500);
  });
  filter();
  if (location.hash) revealHash();
})();
