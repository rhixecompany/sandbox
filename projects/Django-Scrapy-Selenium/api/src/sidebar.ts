const sidebar = document.getElementById('sidebar') as HTMLBodyElement;

if (sidebar) {
    const toggleSidebarMobile = (sidebar: HTMLBodyElement, sidebarBackdrop: HTMLBodyElement, toggleSidebarMobileHamburger: HTMLBodyElement, toggleSidebarMobileClose: HTMLBodyElement) => {
        sidebar.classList.add('flex')
        sidebar.classList.toggle('hidden');
        sidebarBackdrop.classList.toggle('hidden');
        toggleSidebarMobileHamburger.classList.toggle('hidden');
        toggleSidebarMobileClose.classList.toggle('hidden');
    }

    const toggleSidebarMobileEl = document.getElementById('toggleSidebarMobile') as HTMLBodyElement;
    const sidebarBackdrop = document.getElementById('sidebarBackdrop') as HTMLBodyElement;
    const toggleSidebarMobileHamburger = document.getElementById('toggleSidebarMobileHamburger') as HTMLBodyElement;
    const toggleSidebarMobileClose = document.getElementById('toggleSidebarMobileClose') as HTMLBodyElement;
    const toggleSidebarMobileSearch = document.getElementById('toggleSidebarMobileSearch') as HTMLBodyElement;

    toggleSidebarMobileSearch.addEventListener('click', () => {
        toggleSidebarMobile(sidebar, sidebarBackdrop, toggleSidebarMobileHamburger, toggleSidebarMobileClose);
    });

    toggleSidebarMobileEl.addEventListener('click', () => {
        toggleSidebarMobile(sidebar, sidebarBackdrop, toggleSidebarMobileHamburger, toggleSidebarMobileClose);
    });

    sidebarBackdrop.addEventListener('click', () => {
        toggleSidebarMobile(sidebar, sidebarBackdrop, toggleSidebarMobileHamburger, toggleSidebarMobileClose);
    });
}
