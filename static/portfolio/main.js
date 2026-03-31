/*-------------------------------------------
- Personal Portfolio by Raj Kumar Nepal
- URL: https://rajkumarnepal.com.np
- Author: Raj Kumar Nepal
- Made in: January 2025
- Version: 1.0
- For: Assignment Submission
------------------------------------------*/
/* Header toggle */
let MenuBtn = document.getElementById('MenuBtn');
if (MenuBtn) {
    MenuBtn.addEventListener('click', function (e) {
        document.querySelector('body').classList.toggle('mobile-nav-active');
        this.classList.toggle('fa-xmark');
    });
}

/* --- Advanced Scrollspy using IntersectionObserver --- */
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('nav ul li a');

const options = {
    root: null,
    rootMargin: '-20% 0px -70% 0px', // Detects when section is in the top/middle of the viewport
    threshold: 0
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const id = entry.target.getAttribute('id');
            
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${id}`) {
                    link.classList.add('active');
                }
            });
        }
    });
}, options);

sections.forEach(section => {
    observer.observe(section);
});

// Fallback for the very top of the page (Home section)
window.addEventListener('scroll', () => {
    if (window.scrollY < 100) {
        navLinks.forEach(link => link.classList.remove('active'));
        const homeLink = document.querySelector('nav ul li a[href="#home"]');
        if (homeLink) homeLink.classList.add('active');
    }
});
