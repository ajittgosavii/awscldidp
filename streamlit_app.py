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

/* ===== NAVIGATION FIX V2 - AGGRESSIVE MULTI-ROW LAYOUT ===== */
/* MUCH STRONGER CSS TO FORCE WRAPPING */

/* Target ALL button containers and force wrapping */
.stHorizontalBlock,
.horizontal-block,
div[data-testid="stHorizontalBlock"],
div[data-testid="column"]:has(button),
.row-widget,
.element-container:has(button) {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 8px !important;
    max-width: 100% !important;
    overflow: visible !important;
}

/* Force buttons to fixed width and allow wrapping */
.stButton,
button[kind="secondary"],
button[kind="primary"],
div.stButton,
.stButton > button,
button {
    flex: 0 0 auto !important;
    width: 165px !important;
    max-width: 165px !important;
    min-width: 165px !important;
    margin: 4px !important;
    display: inline-block !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
}

/* Specifically target navigation button rows */
div[class*="row"] {
    display: flex !important;
    flex-wrap: wrap !important;
    max-width: 100% !important;
}

/* Force flex containers to wrap */
[class*="st-"] {
    flex-wrap: wrap !important;
}

/* Override any nowrap settings */
* {
    white-space: normal !important;
}

button {
    white-space: nowrap !important;
}

/* Container max-width to force wrapping */
.main .block-container {
    max-width: 100% !important;
}

/* Responsive breakpoints */
@media (max-width: 1600px) {
    .stButton > button,
    button {
        width: 150px !important;
        max-width: 150px !important;
        min-width: 150px !important;
        font-size: 13px !important;
    }
}

@media (max-width: 1400px) {
    .stButton > button,
    button {
        width: 140px !important;
        max-width: 140px !important;
        min-width: 140px !important;
        font-size: 12px !important;
        padding: 8px 12px !important;
    }
}

@media (max-width: 1200px) {
    .stButton > button,
    button {
        width: 130px !important;
        max-width: 130px !important;
        min-width: 130px !important;
        font-size: 11px !important;
        padding: 8px 10px !important;
    }
}

@media (max-width: 1024px) {
    .stButton > button,
    button {
        width: 120px !important;
        max-width: 120px !important;
        min-width: 120px !important;
        font-size: 11px !important;
    }
}

@media (max-width: 768px) {
    .stButton > button,
    button {
        width: 100% !important;
        max-width: 100% !important;
        min-width: 100% !important;
    }
}
/* ===== END NAVIGATION FIX V2 ===== */

</style>

<script>
// JAVASCRIPT NAVIGATION FIX - Guaranteed to work!
function fixNavigationLayout() {
    // Find all button containers
    const containers = document.querySelectorAll('[class*="horizontal"], [class*="row"], .stHorizontalBlock, div[data-testid="stHorizontalBlock"]');
    
    containers.forEach(container => {
        const buttons = container.querySelectorAll('button');
        if (buttons.length >= 5) {
            // This looks like navigation - force flex wrap
            container.style.setProperty('display', 'flex', 'important');
            container.style.setProperty('flex-wrap', 'wrap', 'important');
            container.style.setProperty('gap', '8px', 'important');
            container.style.setProperty('max-width', '100%', 'important');
            container.style.setProperty('overflow', 'visible', 'important');
        }
    });
    
    // Force navigation buttons to fixed width
    const allButtons = document.querySelectorAll('button');
    allButtons.forEach(button => {
        // Only target buttons that look like navigation (have icons/emojis)
        if (button.textContent.match(/[🏠📦🌐🏢📐🔧🚀⚙️🔬👥]/)) {
            button.style.setProperty('flex', '0 0 auto', 'important');
            button.style.setProperty('width', '165px', 'important');
            button.style.setProperty('min-width', '165px', 'important');
            button.style.setProperty('max-width', '165px', 'important');
            button.style.setProperty('margin', '4px', 'important');
            button.style.setProperty('display', 'inline-block', 'important');
        }
    });
}

// Run immediately and on all page changes
fixNavigationLayout();
setTimeout(fixNavigationLayout, 100);
setTimeout(fixNavigationLayout, 500);
setTimeout(fixNavigationLayout, 1000);
setInterval(fixNavigationLayout, 2000);

// Run on Streamlit reloads
window.addEventListener('load', fixNavigationLayout);
const observer = new MutationObserver(fixNavigationLayout);
observer.observe(document.body, { childList: true, subtree: true });
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
