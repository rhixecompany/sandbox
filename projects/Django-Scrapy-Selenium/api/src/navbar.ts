const mobileMenuBtn = document.getElementById("mobile-menu-btn") as HTMLBodyElement;
const mobileMenu = document.getElementById("mobile-menu") as HTMLBodyElement;
const mobileMenuBtnClose = document.getElementById("mobile-menu-btn-close") as HTMLBodyElement;

if (mobileMenuBtn) {
    const openMenu = (): void => {
        mobileMenu.classList.remove("hidden");
        mobileMenu.classList.add("block");
    };
    mobileMenuBtn.addEventListener("click", openMenu);
    if (mobileMenuBtnClose) {
        const closeMenu = (): void => {
            mobileMenu.classList.remove("block");
            mobileMenu.classList.add("hidden");
        };
        mobileMenuBtnClose.addEventListener("click", closeMenu);
    }
}
