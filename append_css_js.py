with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

if '.tab-nav' not in css_content:
    new_css = """
/* Tab Navigation */
.tab-nav {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin: 2rem auto;
    max-width: 800px;
    flex-wrap: wrap;
}

.tab-btn {
    padding: 0.8rem 2rem;
    font-size: 1.1rem;
    font-weight: 600;
    border: 2px solid var(--kemendikbud-blue);
    background-color: white;
    color: var(--kemendikbud-blue);
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.tab-btn:hover {
    background-color: #f0f7ff;
}

.tab-btn.active {
    background-color: var(--kemendikbud-blue);
    color: white;
    box-shadow: 0 4px 10px rgba(0, 89, 178, 0.2);
}

.tab-content {
    display: none;
    animation: fadeIn 0.4s ease;
}

.tab-content.active {
    display: block;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
"""
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write(new_css)
    print("CSS updated successfully.")

with open('script.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

if 'function switchTab' not in js_content and 'window.switchTab' not in js_content:
    new_js = """
// Tab Switching Logic
window.switchTab = function(tabId) {
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    document.getElementById(tabId).classList.add('active');
    document.querySelector(`.tab-btn[onclick="switchTab('${tabId}')"]`).classList.add('active');
};
"""
    with open('script.js', 'a', encoding='utf-8') as f:
        f.write(new_js)
    print("JS updated successfully.")

