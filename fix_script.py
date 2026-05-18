with open("script.js", "r", encoding="utf-8") as f:
    content = f.read()

old_js = """    const slides = Array.from(track.children);
    let currentIndex = 0;
    
    function moveToSlide(index) {
        if (slides.length === 0) return;
        track.style.transform = `translateX(-${index * 100}%)`;
    }
    
    function autoSlide() {
        if (slides.length <= 1) return;
        currentIndex++;
        if (currentIndex >= slides.length) {
            currentIndex = 0;
        }
        moveToSlide(currentIndex);
    }"""

new_js = """    let currentIndex = 0;
    
    function moveToSlide(index) {
        const currentSlides = Array.from(track.children);
        if (currentSlides.length === 0) return;
        track.style.transform = `translateX(-${index * 100}%)`;
    }
    
    function autoSlide() {
        const currentSlides = Array.from(track.children);
        if (currentSlides.length <= 1) return;
        currentIndex++;
        if (currentIndex >= currentSlides.length) {
            currentIndex = 0;
        }
        moveToSlide(currentIndex);
    }"""

content = content.replace(old_js, new_js)

with open("script.js", "w", encoding="utf-8") as f:
    f.write(content)

