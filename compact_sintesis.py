with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_sintesis = """/* Sintesis Container */
.sintesis-container {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    border-radius: 24px;
    padding: 3.5rem;
    margin-top: 4rem;
    max-width: 1160px;
    margin-left: auto;
    margin-right: auto;
    display: grid;
    grid-template-columns: 1fr 1.5fr;
    gap: 3rem;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    color: #f8fafc;
}

.sintesis-left {
    display: flex;
    flex-direction: column;
    text-align: left;
}

.sintesis-tag {
    font-size: 0.8rem;
    letter-spacing: 3px;
    color: #34d399; /* emerald accent */
    text-transform: uppercase;
    margin-bottom: 1rem;
    font-weight: 600;
}

.sintesis-left h3 {
    font-size: 2.2rem;
    line-height: 1.3;
    margin-top: 0;
    margin-bottom: 1.5rem;
    color: #f8fafc;
}

.sintesis-left p {
    color: #94a3b8;
    font-size: 1.05rem;
    line-height: 1.7;
    margin-bottom: 0;
}

.sintesis-right {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    text-align: left;
}

.sintesis-box {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 1.8rem;
    transition: all 0.3s ease;
}

.sintesis-box:hover {
    background: rgba(255, 255, 255, 0.08);
    border-color: rgba(52, 211, 153, 0.3);
    transform: translateY(-3px);
}

.sintesis-box h4 {
    color: #34d399;
    font-size: 0.9rem;
    letter-spacing: 2px;
    margin-top: 0;
    margin-bottom: 1rem;
    text-transform: uppercase;
    font-weight: 700;
}

.sintesis-box p {
    color: #cbd5e1;
    font-size: 0.95rem;
    line-height: 1.6;
    margin: 0;
}"""

new_sintesis = """/* Sintesis Container */
.sintesis-container {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    border-radius: 20px;
    padding: 2.2rem 2.5rem;
    margin-top: 2.5rem;
    max-width: 1160px;
    margin-left: auto;
    margin-right: auto;
    display: grid;
    grid-template-columns: 1fr 1.6fr;
    gap: 2rem;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 15px 30px rgba(0,0,0,0.15);
    color: #f8fafc;
}

.sintesis-left {
    display: flex;
    flex-direction: column;
    text-align: left;
    justify-content: center;
}

.sintesis-tag {
    font-size: 0.75rem;
    letter-spacing: 2px;
    color: #34d399; /* emerald accent */
    text-transform: uppercase;
    margin-bottom: 0.8rem;
    font-weight: 600;
}

.sintesis-left h3 {
    font-size: 1.65rem;
    line-height: 1.3;
    margin-top: 0;
    margin-bottom: 1rem;
    color: #f8fafc;
}

.sintesis-left p {
    color: #94a3b8;
    font-size: 0.9rem;
    line-height: 1.55;
    margin-bottom: 0;
}

.sintesis-right {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    text-align: left;
}

.sintesis-box {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 1.2rem 1.4rem;
    transition: all 0.3s ease;
}

.sintesis-box:hover {
    background: rgba(255, 255, 255, 0.08);
    border-color: rgba(52, 211, 153, 0.3);
    transform: translateY(-2px);
}

.sintesis-box h4 {
    color: #34d399;
    font-size: 0.85rem;
    letter-spacing: 1.5px;
    margin-top: 0;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
    font-weight: 700;
}

.sintesis-box p {
    color: #cbd5e1;
    font-size: 0.85rem;
    line-height: 1.45;
    margin: 0;
}"""

if old_sintesis in css:
    css = css.replace(old_sintesis, new_sintesis)
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Sintesis CSS updated to be compact.")
else:
    print("Could not find old sintesis CSS.")
