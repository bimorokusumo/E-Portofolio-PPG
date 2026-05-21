new_css = """
/* ========================================================================= */
/* TWO-COLUMN SPLIT LAYOUT                                                   */
/* ========================================================================= */
.split-layout {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    width: 100%;
}
.split-layout.align-start {
    align-items: flex-start;
}
.split-left {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}
.split-right {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

@media (max-width: 992px) {
    .split-layout {
        grid-template-columns: 1fr;
        gap: 2rem;
    }
}
"""

with open("style.css", "a", encoding="utf-8") as f:
    f.write(new_css)
print("Added split-layout to style.css")
