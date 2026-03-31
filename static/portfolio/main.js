/*-------------------------------------------
- Personal Portfolio by Raj Kumar Nepal
- URL: https://rajkumarnepal.com.np
- Author: Raj Kumar Nepal
- Made in: January 2025
- Version: 1.0
- For: Assignment Submission
------------------------------------------*/
/* Header toggle */
let MenuBtn = document.getElementById('MenuBtn')

MenuBtn.addEventListener('click', function (e) {
    document.querySelector('body').classList.toggle('mobile-nav-active')
    this.classList.toggle('fa-xmark')
}
)


/* Active Link */

// Getting all the links
let navLinks = document.querySelectorAll('nav ul li a');
// Getting all the sections
let sections = document.querySelectorAll('section');

// Function to check the active link
window.addEventListener('scroll', function() {
    const scrollPos = window.scrollY + 20; // Adding 20px offset for better accuracy
    sections.forEach(section => {
        if(scrollPos > section.offsetTop && scrollPos < (section.offsetTop + section.offsetHeight)) {
            navLinks.forEach(link => {
                link.classList.remove('active'); // Remove 'active' class from all links
                if(section.getAttribute('id') === link.getAttribute('href').substring(1)) {
                    link.classList.add('active'); // Add 'active' class to the correct link
                }
            });
        }
    });
});
