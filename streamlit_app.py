"""
Cloud Infrastructure Development Platform - Enterprise Multi-Account Cloud Management
Simple Blue Theme - Clean & Professional
"""

import streamlit as st
from datetime import datetime
import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

from config_settings import AppConfig
from core_session_manager import SessionManager
from components_navigation import Navigation
from components_sidebar import GlobalSidebar

# Page configuration
st.set_page_config(
    page_title="Cloud Infrastructure Development Platform",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================================================
# SIMPLE BLUE THEME - CLEAN & PROFESSIONAL
# ==================================================================================
st.markdown("""
<style>
/* ===== GLOBAL THEME ===== */
:root {
    --primary-color: #2E86DE;
    --secondary-color: #0652DD;
    --background-color: #FFFFFF;
    --text-color: #000000;
    --border-color: #E0E0E0;
}

/* Main app background - WHITE */
.main {
    background-color: white !important;
}

/* All text - BLACK */
body, p, span, div, label, h1, h2, h3, h4, h5, h6 {
    color: black !important;
}

/* ===== SIDEBAR ===== */
[data-testid="stSidebar"] {
    background-color: #F5F7FA !important;
}

[data-testid="stSidebar"] * {
    color: black !important;
}

/* ===== HEADERS ===== */
h1, h2, h3 {
    color: #2E86DE !important;
}

/* ===== BUTTONS ===== */
button {
    background-color: #2E86DE !important;
    color: white !important;
    border: none !important;
    border-radius: 4px !important;
    padding: 8px 16px !important;
    font-weight: 500 !important;
}

button:hover {
    background-color: #0652DD !important;
    color: white !important;
}

/* ===== DROPDOWNS & SELECTS ===== */
/* Dropdown labels */
.stSelectbox label,
.stMultiSelect label,
.stTextInput label,
.stNumberInput label,
.stTextArea label {
    color: black !important;
    font-weight: 500 !important;
}

/* Dropdown options text - BLACK */
div[data-baseweb="select"] [role="option"],
div[data-baseweb="select"] li,
[role="option"] {
    color: black !important;
    background-color: white !important;
}

/* Dropdown selected value - BLACK */
div[data-baseweb="select"] > div {
    color: black !important;
    background-color: white !important;
}

/* Multiselect tags */
div[data-baseweb="tag"] {
    background-color: #2E86DE !important;
}

div[data-baseweb="tag"] span {
    color: white !important;
}

/* ===== INPUT FIELDS ===== */
input, textarea {
    background-color: white !important;
    color: black !important;
    border: 1px solid #E0E0E0 !important;
}

/* ===== TABS ===== */
.stTabs [data-baseweb="tab-list"] {
    background-color: white !important;
}

.stTabs [data-baseweb="tab"] {
    color: black !important;
}

.stTabs [aria-selected="true"] {
    color: #2E86DE !important;
    border-bottom: 2px solid #2E86DE !important;
}

/* ===== METRICS ===== */
/* Let aws_theme.py handle metric styling - don't override! */
.stMetric {
    background-color: transparent !important;
}

/* ===== INFO/WARNING/ERROR BOXES ===== */
.stAlert {
    background-color: white !important;
    border-left: 4px solid #2E86DE !important;
}

/* ===== DATAFRAMES ===== */
.stDataFrame {
    background-color: white !important;
}

table {
    background-color: white !important;
}

th {
    background-color: #2E86DE !important;
    color: white !important;
}

td {
    color: black !important;
}

/* ===== EXPANDERS ===== */
.streamlit-expanderHeader {
    background-color: #F5F7FA !important;
    color: black !important;
}

/* ===== RADIO & CHECKBOX ===== */
.stRadio label,
.stCheckbox label {
    color: black !important;
}

/* ===== CLEAN BORDERS ===== */
.stSelectbox > div,
.stMultiSelect > div,
.stTextInput > div,
.stNumberInput > div {
    border-radius: 4px !important;
}

/* ===== NAVIGATION SCROLL BUTTONS ===== */
/* Safe scroll button implementation */

/* Add padding to navigation area for scroll buttons */
[data-testid="stHorizontalBlock"]:has(button) {
    padding: 0 60px !important;
    position: relative !important;
    overflow-x: auto !important;
    overflow-y: hidden !important;
    scroll-behavior: smooth !important;
    -webkit-overflow-scrolling: touch !important;
}

/* Hide scrollbar but keep functionality */
[data-testid="stHorizontalBlock"]:has(button)::-webkit-scrollbar {
    height: 6px !important;
}

[data-testid="stHorizontalBlock"]:has(button)::-webkit-scrollbar-track {
    background: rgba(46, 134, 222, 0.1) !important;
    border-radius: 3px !important;
}

[data-testid="stHorizontalBlock"]:has(button)::-webkit-scrollbar-thumb {
    background: rgba(46, 134, 222, 0.5) !important;
    border-radius: 3px !important;
}

[data-testid="stHorizontalBlock"]:has(button)::-webkit-scrollbar-thumb:hover {
    background: #2E86DE !important;
}

/* Style for scroll buttons - will be added with JavaScript */
.nav-scroll-btn {
    position: fixed !important;
    top: 230px !important;
    width: 45px !important;
    height: 45px !important;
    background: #2E86DE !important;
    color: white !important;
    border: none !important;
    border-radius: 50% !important;
    cursor: pointer !important;
    font-size: 20px !important;
    font-weight: bold !important;
    z-index: 1000 !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3) !important;
    transition: all 0.3s ease !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}

.nav-scroll-btn:hover {
    background: #0652DD !important;
    transform: scale(1.1) !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4) !important;
}

.nav-scroll-btn:active {
    transform: scale(0.95) !important;
}

.nav-scroll-btn-left {
    left: 220px !important;
}

.nav-scroll-btn-right {
    right: 20px !important;
}

/* Hide buttons when not needed */
.nav-scroll-btn.hidden {
    opacity: 0 !important;
    pointer-events: none !important;
}

/* ===== END NAVIGATION SCROLL BUTTONS ===== */

</style>

<script>
// Simple, safe scroll button implementation
(function() {
    let navContainer = null;
    let leftBtn = null;
    let rightBtn = null;
    
    function findNavContainer() {
        const blocks = document.querySelectorAll('[data-testid="stHorizontalBlock"]');
        for (let block of blocks) {
            if (block.querySelectorAll('button').length >= 8) {
                return block;
            }
        }
        return null;
    }
    
    function createScrollButtons() {
        if (leftBtn && rightBtn) return; // Already created
        
        // Create left button
        leftBtn = document.createElement('button');
        leftBtn.innerHTML = '◀';
        leftBtn.className = 'nav-scroll-btn nav-scroll-btn-left';
        leftBtn.onclick = () => scrollNav(-300);
        
        // Create right button
        rightBtn = document.createElement('button');
        rightBtn.innerHTML = '▶';
        rightBtn.className = 'nav-scroll-btn nav-scroll-btn-right';
        rightBtn.onclick = () => scrollNav(300);
        
        document.body.appendChild(leftBtn);
        document.body.appendChild(rightBtn);
    }
    
    function scrollNav(amount) {
        if (navContainer) {
            navContainer.scrollBy({ left: amount, behavior: 'smooth' });
            setTimeout(updateButtonVisibility, 100);
        }
    }
    
    function updateButtonVisibility() {
        if (!navContainer || !leftBtn || !rightBtn) return;
        
        const scrollLeft = navContainer.scrollLeft;
        const maxScroll = navContainer.scrollWidth - navContainer.clientWidth;
        
        // Hide left button if at start
        if (scrollLeft <= 10) {
            leftBtn.classList.add('hidden');
        } else {
            leftBtn.classList.remove('hidden');
        }
        
        // Hide right button if at end
        if (scrollLeft >= maxScroll - 10) {
            rightBtn.classList.add('hidden');
        } else {
            rightBtn.classList.remove('hidden');
        }
    }
    
    function init() {
        navContainer = findNavContainer();
        if (navContainer) {
            createScrollButtons();
            updateButtonVisibility();
            
            // Update on scroll
            navContainer.addEventListener('scroll', updateButtonVisibility);
            
            // Update on window resize
            window.addEventListener('resize', updateButtonVisibility);
        }
    }
    
    // Initialize when page loads
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
    // Re-check after Streamlit renders
    setTimeout(init, 500);
    setTimeout(init, 1000);
})();
</script>

""", unsafe_allow_html=True)
# ==================================================================================
# END SIMPLE BLUE THEME
# ==================================================================================

# Simple header - centered
st.markdown("""
<div style="background: linear-gradient(135deg, #2E86DE 0%, #0652DD 100%); padding: 20px; border-radius: 10px; margin-bottom: 20px; text-align: center;">
    <h1 style="color: white !important; margin: 0; font-weight: 600;">☁️ Cloud Infrastructure Development Platform</h1>
    <p style="color: white !important; margin: 5px 0 0 0; font-size: 16px;">Enterprise Multi-Account Cloud Management</p>
</div>
""", unsafe_allow_html=True)

def main():
    """Main application entry point"""
    
    # Initialize session
    SessionManager.initialize()
    
    # Render global sidebar
    GlobalSidebar.render()
    
    # Render main navigation
    Navigation.render()
    
    # Simple footer
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.caption(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    with col2:
        st.caption(f"🔗 Connected Accounts: {SessionManager.get_active_account_count()}")
    with col3:
        st.caption("☁️ Cloud Infrastructure Development Platform")

if __name__ == "__main__":
    main()
