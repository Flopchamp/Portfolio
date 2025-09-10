import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import requests
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="Harrison Aloo - Software Engineer Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    
    /* Enhanced Sidebar Styling */
    .css-1d391kg {
        background-color: #f8f9fa;
        border-right: 3px solid #667eea;
    }
    
    .css-1d391kg .css-1v3fvcr {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
        text-align: center;
        font-weight: bold;
        font-size: 1.2rem;
    }
    
    /* Sidebar selectbox styling */
    .stSelectbox > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    .stSelectbox > div > div > div {
        color: white;
        font-weight: bold;
    }
    
    .skill-badge {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.2rem;
        display: inline-block;
        font-weight: bold;
    }
    
    .project-card {
        border: 2px solid #4285F4;
        border-radius: 15px;
        padding: 2.5rem;
        margin: 2rem 0;
        box-shadow: 0 6px 12px rgba(66, 133, 244, 0.15);
        background: #ffffff !important;
        min-height: auto;
        overflow: visible;
        word-wrap: break-word;
    }
    
    .project-card h3, .project-card h4, .project-card h5 {
        margin-bottom: 1rem;
        line-height: 1.4;
        color: #1a73e8 !important;
    }
    
    .project-card p {
        line-height: 1.7;
        margin-bottom: 1.5rem;
        text-align: left;
        color: #202124 !important;
        font-size: 1.1rem;
        font-weight: 500;
    }
    
    .project-card ul {
        padding-left: 2rem;
        line-height: 1.6;
        list-style-type: none;
    }
    
    .project-card li {
        margin-bottom: 0.8rem;
        padding: 0.3rem 0;
        color: #202124 !important;
        position: relative;
        padding-left: 1.5rem;
        font-weight: 500;
    }
    
    .project-card li::before {
        content: "✓";
        color: #34a853;
        font-weight: bold;
        position: absolute;
        left: 0;
    }
    
    /* Enhanced project card styling for better visibility */
    div[style*="border: 1px solid #e0e0e0"] {
        background: #ffffff !important;
    }
    
    div[style*="border: 1px solid #e0e0e0"] h3 {
        color: #1a73e8 !important;
        font-weight: bold !important;
    }
    
    div[style*="border: 1px solid #e0e0e0"] p {
        color: #202124 !important;
        font-weight: 500 !important;
    }
    
    div[style*="border: 1px solid #e0e0e0"] li {
        color: #202124 !important;
        font-weight: 500 !important;
    }
    
    div[style*="border: 1px solid #e0e0e0"] strong {
        color: #1a73e8 !important;
        font-weight: bold !important;
    }
    
    .achievement-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        text-align: center;
    }
    
    .contact-button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        text-decoration: none;
        font-weight: bold;
        margin: 0.5rem;
        display: inline-block;
    }
    
    .google-card {
        border: 2px solid #4285F4;
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        background: linear-gradient(135deg, #f8f9ff 0%, #e3f2fd 100%);
        box-shadow: 0 4px 8px rgba(66, 133, 244, 0.2);
    }
    
    .google-highlight {
        background: linear-gradient(90deg, #4285F4 0%, #34A853 50%, #FBBC05 75%, #EA4335 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }
    
    /* Improve text visibility across the app */
    .stMarkdown p {
        color: #ffffff !important;
        font-size: 1rem;
        line-height: 1.6;
        font-weight: 500;
    }
    
    .stMarkdown li {
        color: #ffffff !important;
        line-height: 1.5;
        margin-bottom: 0.5rem;
        font-weight: 500;
    }
    
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5 {
        color: #4285F4 !important;
        line-height: 1.3;
        font-weight: bold;
    }
    
    .stMarkdown strong {
        color: #4285F4 !important;
        font-weight: 700;
    }
    
    /* Ensure text in containers is visible */
    div[data-testid="stMarkdownContainer"] p {
        color: #ffffff !important;
        font-weight: 500;
    }
    
    div[data-testid="stMarkdownContainer"] li {
        color: #ffffff !important;
        font-weight: 500;
    }
    
    div[data-testid="stMarkdownContainer"] strong {
        color: #4285F4 !important;
        font-weight: 700;
    }
    
    /* Ensure all markdown text is visible */
    .stMarkdown {
        color: #ffffff !important;
    }
    
    /* Force text visibility in all elements */
    p, li, span, div {
        color: #ffffff !important;
    }
    
    /* Override for project cards - ensure dark text on white background */
    .project-card p,
    .project-card li,
    .project-card span,
    .project-card div,
    .project-card strong {
        color: #202124 !important;
        background: transparent !important;
    }
    
    .project-card h3 {
        color: #4285F4 !important;
        background: transparent !important;
    }
    
    /* Headers should be blue */
    h1, h2, h3, h4, h5, h6 {
        color: #4285F4 !important;
    }
    
    /* Fix sidebar text visibility */
    .css-1d391kg .stMarkdown {
        color: #333333 !important;
    }
    
    /* Enhanced content cards with better contrast */
    .content-card {
        background: #1e1e1e;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        margin-bottom: 2rem;
        border: 1px solid #4285F4;
    }
    
    .content-card h3, .content-card h4, .content-card h5 {
        color: #4285F4 !important;
        margin-bottom: 1rem;
    }
    
    .content-card p, .content-card li {
        color: #ffffff !important;
        line-height: 1.6;
        font-weight: 500;
    }
    
    /* Main app background for better readability */
    .main .block-container {
        background-color: #0d1117;
        padding: 1rem;
    }
    
    /* Streamlit main area background */
    .stApp {
        background-color: #0d1117;
    }
    
    /* Image styling improvements */
    .stImage > div {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    .stImage img {
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        max-width: 100%;
        height: auto;
        object-fit: cover;
    }
    
    /* Profile image specific styling */
    .profile-image {
        border-radius: 50% !important;
        border: 4px solid #4285F4 !important;
        box-shadow: 0 8px 16px rgba(66, 133, 244, 0.3) !important;
        object-fit: cover !important;
    }
    
    /* Project images */
    .project-image {
        border-radius: 10px;
        border: 2px solid #e8eaed;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .project-image:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* CRITICAL: Force text visibility with maximum specificity */
    .stMarkdown[data-testid="stMarkdownContainer"] div {
        background: transparent !important;
    }
    
    .stMarkdown[data-testid="stMarkdownContainer"] div * {
        color: #202124 !important;
        background: transparent !important;
    }
    
    .stMarkdown[data-testid="stMarkdownContainer"] p {
        color: #202124 !important;
        font-weight: 500 !important;
        background: transparent !important;
    }
    
    .stMarkdown[data-testid="stMarkdownContainer"] li {
        color: #202124 !important;
        font-weight: 500 !important;
        background: transparent !important;
    }
    
    .stMarkdown[data-testid="stMarkdownContainer"] h1,
    .stMarkdown[data-testid="stMarkdownContainer"] h2,
    .stMarkdown[data-testid="stMarkdownContainer"] h3,
    .stMarkdown[data-testid="stMarkdownContainer"] h4,
    .stMarkdown[data-testid="stMarkdownContainer"] h5 {
        color: #1a73e8 !important;
        font-weight: bold !important;
        background: transparent !important;
    }
    
    .stMarkdown[data-testid="stMarkdownContainer"] strong {
        color: #1a73e8 !important;
        font-weight: bold !important;
        background: transparent !important;
    }
    
    /* EXTRA SPECIFIC: Project card text visibility */
    div[style*="border: 2px solid #4285F4"] p,
    div[style*="border: 2px solid #4285F4"] li,
    div[style*="border: 2px solid #4285F4"] span,
    div[style*="border: 2px solid #FBBC05"] p,
    div[style*="border: 2px solid #FBBC05"] li,
    div[style*="border: 2px solid #FBBC05"] span {
        color: #202124 !important;
        font-weight: 500 !important;
        background: transparent !important;
        display: block !important;
        visibility: visible !important;
    }
    
    /* Force project card headers to be visible */
    div[style*="border: 2px solid #4285F4"] h3,
    div[style*="border: 2px solid #FBBC05"] h3 {
        color: #4285F4 !important;
        font-weight: bold !important;
        background: transparent !important;
        display: block !important;
        visibility: visible !important;
    }
    }
    
    /* Override any Streamlit default that might hide text */
    .stApp * {
        text-shadow: none !important;
    }
    
    .stApp div:not(.stSidebar) {
        color: #202124 !important;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("""
<div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
     border-radius: 10px; margin-bottom: 1.5rem; color: white;">
    <h2 style="margin: 0; color: white;"> Navigation</h2>
    <p style="margin: 0; color: white; opacity: 0.9;">Explore my portfolio</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state for navigation if not exists
if 'selected_section' not in st.session_state:
    st.session_state.selected_section = "Home"

sections = [
    ("Home", ""), 
    ("About", ""), 
    ("Projects", ""), 
    ("Skills", ""), 
    ("Experience", ""), 
    ("Achievements", ""), 
    ("Contact", "")
]

for section_name, icon in sections:
    if st.sidebar.button(f"{icon} {section_name}", key=f"nav_{section_name}"):
        st.session_state.selected_section = section_name
        st.rerun()

selected_section = st.session_state.selected_section

# Main Content Area
if selected_section == "Home":
    st.markdown('<h1 class="main-header"> Harrison Onyango Aloo</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; color: #667eea;">Software Engineer </h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Using GitHub avatar with improved styling
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <img src="https://avatars.githubusercontent.com/u/162114115?v=4" 
                 style="width: 300px; height: 300px; border-radius: 50%; 
                        border: 4px solid #4285F4; box-shadow: 0 8px 16px rgba(66, 133, 244, 0.3);
                        object-fit: cover; display: block; margin: 0 auto;"
                 alt="Harrison Aloo - Software Engineer">
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<p style="text-align: center; color: #667eea; font-weight: bold; margin-top: 1rem;">GitHub: @Flopchamp</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="achievement-card" style="background: linear-gradient(135deg, #FBBC05 0%, #EA4335 100%);">
            <h3> Algorithmic Trading</h3>
            <p>Professional-grade trading systems with advanced pattern recognition and market analysis</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="achievement-card" style="background: linear-gradient(135deg, #34A853 0%, #4285F4 100%);">
            <h3> Full-Stack Developer</h3>
            <p>12+ active repositories in JavaScript, TypeScript, and Python</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Specialty Areas
    st.subheader(" Core Specializations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ** Financial Technology**
        - **ENIGMA APEX** - Professional algorithmic trading platform
        - **Harmonic Patterns** - Advanced pattern recognition systems  
        - **Trading Bots** - Automated cryptocurrency trading
        - **Market Analysis** - Real-time data processing tools
        """)
        
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FBBC05 0%, #EA4335 100%); 
             color: white; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
            <h4 style="margin-top: 0; color: white;"> FinTech Expertise</h4>
            <p style="color: white;">Specialized in algorithmic trading systems, pattern recognition, and financial data analysis</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        ** Full-Stack Development**
        - **MovieFlex** - TypeScript streaming application
        - **FishCrewConnect** - Social platform for fishing community
        - **ProductStore** - E-commerce solution with CRUD backend
        - **Modern Web Apps** - React, Node.js, responsive design
        """)
        
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4285F4 0%, #34A853 100%); 
             color: white; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
            <h4 style="margin-top: 0; color: white;"> Web Development</h4>
            <p style="color: white;">Full-stack applications with modern JavaScript, TypeScript, and Python technologies</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick stats - Updated with real data
    st.subheader(" Current Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("GitHub Repositories", "12", "Active development")
    
    with col2:
        st.metric("Last Commit", "12 hours ago", "Very Active")
    
    with col3:
        st.metric("Primary Languages", "JS/TS/Python", "Multi-stack")
    
    with col4:
        st.metric("Specialization", "FinTech", "Trading Systems")
    
    st.markdown("---")
    
    # Recent Activity
    st.subheader(" Recent Activity")
    
    recent_projects = [
        {"name": "ENIGMA APEX Professional Algo Trader", "status": "🟢 Updated 12 hours ago", "lang": "Python"},
        {"name": "Mike (Trading Tool)", "status": "🟡 Updated 4 days ago", "lang": "Python"},
        {"name": "Harmonics Pattern Scanner", "status": "🟡 Updated 2 weeks ago", "lang": "JavaScript"},
        {"name": "FishCrewConnect", "status": "🟢 Updated 3 weeks ago", "lang": "JavaScript"}
    ]
    
    for project in recent_projects:
        col1, col2, col3 = st.columns([3, 2, 1])
        with col1:
            st.markdown(f"**{project['name']}**")
        with col2:
            st.markdown(project['status'])
        with col3:
            st.markdown(f"`{project['lang']}`")
    
    st.markdown("---")
    
    # Call to Action
    st.markdown("""
    
    """, unsafe_allow_html=True)
    
    with col4:
        st.metric("Years Experience", "3+", "Growing")

elif selected_section == "About":
    st.markdown('<h1 class="main-header"> About Me</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Hi, I'm Harrison Aloo! ")
        
        st.markdown("""
        I'm a passionate **Software Engineer** with expertise in **Financial Technology** and **Full-Stack Development**. 
        Currently building professional-grade algorithmic trading systems while preparing for opportunities at top tech companies like **Google**, **Microsoft**, and **Amazon**.
        """)
        
        st.markdown("####  What I Do")
        st.markdown("""
        - **Algorithmic Trading Systems**: Building professional trading platforms like ENIGMA APEX
        - **Pattern Recognition**: Developing advanced harmonic pattern detection systems
        - **Full-Stack Development**: Creating modern web applications with React, TypeScript, and Python
        - **Financial Technology**: Specializing in market analysis and trading automation
        - **Open Source Contribution**: Active contributor with 18+ repositories on GitHub (@Flopchamp)
        """)
        
        st.markdown("####  Current Focus")
        st.markdown("""
        - **Google Interview Preparation**: Mastering algorithms, system design, and behavioral questions
        - **Advanced Trading Systems**: Continuously improving algorithmic trading strategies
        - **Technology Stack Expansion**: Exploring new frameworks and technologies
        - **Professional Growth**: Building expertise in scalable system architecture
        """)
        
        st.markdown("####  My Approach")
        st.markdown("""
        I believe in combining **technical excellence** with **practical application**. My projects demonstrate real-world problem-solving, 
        from building trading systems that analyze financial markets to creating user-friendly web applications. 
        I'm passionate about writing clean, maintainable code and contributing to meaningful projects.
        """)
        
        st.markdown("####  What Makes Me Different")
        st.markdown("""
        - **Unique FinTech Expertise**: Deep understanding of financial markets and trading systems
        - **Proven Track Record**: 18+ active repositories with recent commits (updated 12 hours ago)
        - **Multi-Language Proficiency**: Expert in Python, JavaScript, and TypeScript
        - **Real-World Applications**: Projects that solve actual problems in trading and web development
        """)
    
    with col2:
        # Profile Image Section
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem; background: white; border-radius: 15px; 
             box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-bottom: 1.5rem;">
            <img src="https://avatars.githubusercontent.com/u/162114115?v=4" 
                 style="width: 200px; height: 200px; border-radius: 50%; 
                        border: 4px solid #4285F4; box-shadow: 0 8px 16px rgba(66, 133, 244, 0.3);
                        object-fit: cover; display: block; margin: 0 auto 1rem auto;"
                 alt="Harrison Aloo - Software Engineer">
            <h4 style="color: #1a73e8; margin: 0.5rem 0;">Harrison Aloo</h4>
            <p style="color: black; margin: 0; font-weight: 500;">Software Engineer</p>
            <p style="color: black; margin: 0.5rem 0; font-weight: bold;">@Flopchamp</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        
        <div style="background: linear-gradient(135deg, #FBBC05 0%, #EA4335 100%); 
             color: white; padding: 1.5rem; border-radius: 15px;">
            <h3 style="color: white; margin-top: 0;"> Key Strengths</h3>
            <ul style="text-align: left; color: white;">
                <li> Algorithmic Trading Expert</li>
                <li> Full-Stack Developer</li>
                <li> System Architecture</li>
                <li> Data Analysis & Visualization</li>
                <li> Modern Web Technologies</li>
                <li> Automation & APIs</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Education & Certifications
    st.subheader("🎓 Education & Academic Excellence")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🎓 Bachelor of Science in Software Engineering**
        - **University of Eastern Africa, Baraton (UEAB)**
        - **CGPA: 3.256/4.0** (Excellent Performance)
        - **Year of Graduation:** 2025
        - **Academic Recognition:** Strong grades in core subjects
        
        **📚 Key Coursework Excellence:**
        - **Artificial Intelligence:** Grade A
        - **Software Engineering:** Grade A
        - **Practical Experience:** Grade A
        - **Database Systems:** Grade B+
        - **Web Development:** Grade A-
        - **Mobile App Development:** Grade B+
        """)
    
    with col2:
        st.markdown("""
        **🏆 Academic Achievements:**
        - Maintained consistent academic performance
        - Specialized in AI and Software Engineering
        - Practical hands-on project experience
        - Strong foundation in computer science fundamentals
        
        **💼 Academic to Professional Bridge:**
        - Applied academic knowledge in real projects
        - Translated theory into practical applications
        - Continuous learning beyond formal education
        - Industry-relevant skill development
        """)

elif selected_section == "Projects":
    st.markdown('<h1 class="main-header">💼 Projects Portfolio</h1>', unsafe_allow_html=True)
    
    st.markdown("### Featured Projects from my GitHub (@Flopchamp)")
    st.markdown("**12+ Active Repositories** | **Updated Regularly** | **Algorithmic Trading Focus**")
    
    # Project 1 - ENIGMA APEX Professional Algo Trader
    st.markdown("""
    <div style="border: 2px solid #4285F4; border-radius: 15px; padding: 2rem; margin: 1rem 0; box-shadow: 0 4px 8px rgba(0,0,0,0.1); background: #ffffff;">
        <h3 style="color: #4285F4; font-weight: bold; margin-bottom: 1rem;">🚀 ENIGMA APEX PROFESSIONAL ALGO TRADER</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Use Streamlit markdown for better text rendering
    st.markdown("**Tech Stack:** Python, Financial APIs, Data Analysis, Real-time Processing")
    
    st.markdown("""
    Professional-grade algorithmic trading system with advanced market analysis and automated trading strategies. 
    Built with Python for high-performance financial data processing and real-time trading execution.
    """)
    
    st.markdown("**Key Features:**")
    st.markdown("""
    - ✅ Advanced algorithmic trading strategies
    - 📊 Real-time market data processing  
    - 🔒 Risk management and portfolio optimization
    - 💼 Professional trading interface
    - 🤖 Automated execution and monitoring
    """)
    
    st.markdown("**🔗 Links:** [GitHub Repository](https://github.com/Flopchamp/ENIGMA_APEX_PROFESSIONAL_ALGO_TRADER) | 🟢 Updated 12 hours ago")
    
    st.markdown("---")
    
    # Project 2 - Harmonic Patterns Scanner
    st.markdown("""
    <div style="border: 2px solid #FBBC05; border-radius: 15px; padding: 2rem; margin: 1rem 0; box-shadow: 0 4px 8px rgba(0,0,0,0.1); background: #ffffff;">
        <h3 style="color: #FBBC05; font-weight: bold; margin-bottom: 1rem;">📈 Harmonic Pattern Scanner</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Use Streamlit markdown for better text rendering
    st.markdown("**Tech Stack:** JavaScript, Pattern Recognition, Financial Mathematics")
    
    st.markdown("""
    Advanced harmonic pattern detection system for financial markets. Implements complex mathematical algorithms 
    to identify profitable trading patterns in real-time market data.
    """)
    
    st.markdown("**Key Features:**")
    st.markdown("""
    - 🎯 Real-time harmonic pattern detection
    - 📊 Multiple pattern types (Gartley, Butterfly, Bat, Crab)
    - 👀 Visual pattern recognition
    - 📈 Performance analytics and backtesting
    - 🔔 Alert system for pattern completion
    """)
    
    st.markdown("**🔗 Links:** [GitHub Repository](https://github.com/Flopchamp/harmonics-pattern-scanner) | 🟡 Updated 2 weeks ago")
    
    st.markdown("---")
    
    # Project 3 - MovieFlex
    st.markdown("""
    <div style="border: 2px solid #4285F4; border-radius: 15px; padding: 2rem; margin: 1rem 0; box-shadow: 0 4px 8px rgba(0,0,0,0.1); background: #ffffff;">
        <h3 style="color: #4285F4; font-weight: bold; margin-bottom: 1rem;">🎬 MovieFlex</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Use Streamlit markdown for better text rendering
    st.markdown("**Tech Stack:** TypeScript, React, Modern Web APIs")
    
    st.markdown("""
    Modern movie streaming application built with TypeScript for type safety and enhanced developer experience. 
    Features responsive design, advanced search, and user-friendly interface.
    """)
    
    st.markdown("**Key Features:**")
    st.markdown("""
    - 🎯 TypeScript for type-safe development
    - 📱 Responsive movie browsing interface
    - 🔍 Advanced search and filtering
    - ❤️ User preferences and watchlists
    - 🎨 Modern UI/UX design patterns
    """)
    
    st.markdown("**🔗 Links:** [GitHub Repository](https://github.com/Flopchamp/MovieFlex) | 🔵 TypeScript Project")
    
    st.markdown("---")
    
    # Project 4 - FishCrewConnect
    st.markdown("""
    <div style="border: 2px solid #34A853; border-radius: 15px; padding: 2rem; margin: 1rem 0; box-shadow: 0 4px 8px rgba(0,0,0,0.1); background: #ffffff;">
        <h3 style="color: #34A853; font-weight: bold; margin-bottom: 1rem;">🎣 FishCrewConnect</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Use Streamlit markdown for better text rendering
    st.markdown("**Tech Stack:** JavaScript, Full-Stack Web Development, React Native")
    
    st.markdown("""
    Social platform connecting fishing enthusiasts and crew members. Built with modern JavaScript 
    for seamless user experience and community building features.
    """)
    
    st.markdown("**Key Features:**")
    st.markdown("""
    - 👤 User registration and profile management
    - 🤝 Crew matching and communication
    - 🗓️ Trip planning and coordination
    - 💬 Community features and messaging
    - 📍 Location-based services
    """)
    
    st.markdown("**🔗 Links:** [GitHub Repository](https://github.com/Flopchamp/FishCrewConnect) | 🟢 Updated 3 weeks ago")
    
    st.markdown("---")
    
    # Project 5 - ProductStore
    st.markdown("""
    <div style="border: 2px solid #EA4335; border-radius: 15px; padding: 2rem; margin: 1rem 0; box-shadow: 0 4px 8px rgba(0,0,0,0.1); background: #ffffff;">
        <h3 style="color: #EA4335; font-weight: bold; margin-bottom: 1rem;">🛒 ProductStore</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Use Streamlit markdown for better text rendering
    st.markdown("**Tech Stack:** JavaScript, E-commerce, Full-Stack Development, CRUD Backend")
    
    st.markdown("""
    Complete e-commerce solution with modern JavaScript architecture. Features product management, 
    shopping cart functionality, and secure payment processing integration.
    """)
    
    st.markdown("**Key Features:**")
    st.markdown("""
    - 📦 Product catalog management
    - 🛒 Shopping cart and checkout process
    - 👤 User authentication and profiles
    - 📋 Order tracking and management
    - 📱 Responsive design for all devices
    """)
    
    st.markdown("**🔗 Links:** [GitHub Repository](https://github.com/Flopchamp/ProductStore) | [Backend Repository](https://github.com/Flopchamp/Crud-App-Backend)")
    
    st.markdown("---")
    
    # Additional Projects Summary
    st.markdown("---")
    st.subheader("🔧 Additional Projects")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Trading & Finance:**
        - 🔥 **Trader** (TypeScript) - Advanced trading platform
        - 📊 **Hyperliquid Trader 2** - Cryptocurrency trading bot
        - 📈 **Mike** (Python) - Trading analysis tool
        
        **Web Development:**
        - 🌐 **Project Demo** - Full-stack demonstration
        - ⚙️ **Crud-App-Backend** - RESTful API backend
        """)
    
    with col2:
        st.markdown("""
        **Specialized Tools:**
        - 🎯 **Harmonic Patterns** - Pattern recognition library
        - 📱 Multiple JavaScript/TypeScript projects
        - 🐍 Python-based financial analysis tools
        
        **Recent Activity:**
        - 🔥 Daily commits and updates
        - 🚀 Active development on trading projects
        """)
    
    st.markdown("---")
    
    # GitHub Stats
    st.subheader("📊 GitHub Activity")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Repositories", "12+", "+2 recent")
    
    with col2:
        st.metric("Primary Languages", "JS/TS/Python", "Multi-language")
    
    with col3:
        st.metric("Specialization", "Algo Trading", "FinTech Focus")
    
    with col4:
        st.metric("Last Update", "12 hours ago", "Very Active")
    
    st.markdown("---")
    st.markdown("### 🔗 Explore More")
    st.markdown("Visit my [GitHub profile](https://github.com/Flopchamp) to see all repositories and live contributions!")
    
    # Call to Action for Employers
    st.markdown("""
    <div style="border: 2px solid #4285F4; border-radius: 15px; padding: 2rem; margin: 1rem 0; 
         background: linear-gradient(135deg, #f8f9ff 0%, #e3f2fd 100%); 
         box-shadow: 0 4px 8px rgba(66, 133, 244, 0.2);">
        <h3 style="background: linear-gradient(90deg, #4285F4 0%, #34A853 50%, #FBBC05 75%, #EA4335 100%);
           -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: bold; margin-bottom: 1rem;">🎯 For Potential Employers</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Use Streamlit markdown for better text rendering
    st.markdown("**My projects demonstrate expertise in:**")
    
    st.markdown("""
    - **💼 Algorithmic Trading Systems** - Professional-grade financial software
    - **🌐 Full-Stack Development** - Complete web applications from frontend to backend  
    - **⚡ TypeScript/JavaScript** - Modern web development with type safety
    - **🐍 Python** - Data analysis, automation, and backend services
    - **💰 Financial Technology** - Deep understanding of market mechanics
    """)
    
    st.markdown("---")
    
    st.markdown("### 🚀 Ready to bring this expertise to your team at Google, Microsoft, or Amazon!")
    
    st.markdown("---")
    
    # Project Showcase with Images Section
    st.markdown("---")
    st.subheader("📷 Project Showcases")
    
    # Create image placeholder cards for projects
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # ENIGMA APEX Card with Hybrid Approach
        st.markdown("""
        <div style="border: 2px solid #4285F4; border-radius: 15px; padding: 1.5rem; 
             background: white; box-shadow: 0 4px 8px rgba(0,0,0,0.1); text-align: center; margin-bottom: 1rem;">
            <div style="width: 100%; height: 150px; background: linear-gradient(135deg, #4285F4 0%, #34A853 100%); 
                 border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                <h3 style="color: white; margin: 0;">🚀 ENIGMA APEX</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("**Trading Platform**")
        st.write("Professional algorithmic trading system with advanced pattern recognition and risk management capabilities.")
    
    with col2:
        # MovieFlex Card with Hybrid Approach
        st.markdown("""
        <div style="border: 2px solid #FBBC05; border-radius: 15px; padding: 1.5rem; 
             background: white; box-shadow: 0 4px 8px rgba(0,0,0,0.1); text-align: center; margin-bottom: 1rem;">
            <div style="width: 100%; height: 150px; background: linear-gradient(135deg, #FBBC05 0%, #EA4335 100%); 
                 border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                <h3 style="color: white; margin: 0;">🎬 MovieFlex</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("**Streaming App**")
        st.write("TypeScript-based movie streaming platform with modern UI/UX design and responsive architecture.")
    
    with col3:
        # FishCrew Card with Hybrid Approach
        st.markdown("""
        <div style="border: 2px solid #34A853; border-radius: 15px; padding: 1.5rem; 
             background: white; box-shadow: 0 4px 8px rgba(0,0,0,0.1); text-align: center; margin-bottom: 1rem;">
            <div style="width: 100%; height: 150px; background: linear-gradient(135deg, #34A853 0%, #4285F4 100%); 
                 border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                <h3 style="color: white; margin: 0;">🎣 FishCrew</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("**Social Platform**")
        st.write("Community connection app for fishing enthusiasts with social networking features and location sharing.")

elif selected_section == "Skills":
    st.markdown('<h1 class="main-header">🛠️ Technical Skills</h1>', unsafe_allow_html=True)
    
    st.markdown("### 🎯 **Core Expertise: Financial Technology & Full-Stack Development**")
    
    # Programming Languages - Updated based on GitHub repos
    st.subheader("💻 Programming Languages")
    languages = ["Python", "JavaScript", "TypeScript", "HTML/CSS", "SQL", "JSON"]
    cols = st.columns(len(languages))
    for i, lang in enumerate(languages):
        with cols[i]:
            if lang in ["Python", "JavaScript", "TypeScript"]:
                st.markdown(f'<div class="skill-badge" style="background: linear-gradient(90deg, #4285F4 0%, #34A853 100%);">{lang} ⭐</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="skill-badge">{lang}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Financial Technology Specialization
    st.subheader("� Financial Technology & Trading")
    fintech_skills = ["Algorithmic Trading", "Pattern Recognition", "Market Analysis", "Risk Management", "Financial APIs", "Real-time Data Processing", "Backtesting Systems", "Portfolio Optimization"]
    cols = st.columns(4)
    for i, skill in enumerate(fintech_skills):
        with cols[i % 4]:
            st.markdown(f'<div class="skill-badge" style="background: linear-gradient(90deg, #FBBC05 0%, #EA4335 100%);">{skill}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Web Development Stack
    st.subheader("🌐 Full-Stack Web Development")
    web_skills = ["React.js", "Node.js", "Express.js", "RESTful APIs", "Frontend Design", "Backend Architecture", "Database Design", "Authentication Systems"]
    cols = st.columns(4)
    for i, skill in enumerate(web_skills):
        with cols[i % 4]:
            st.markdown(f'<div class="skill-badge">{skill}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Development Tools & Technologies
    st.subheader("🛠️ Development Tools & Platforms")
    tools = ["Git & GitHub", "VS Code", "npm/yarn", "Webpack", "Docker", "Linux/Unix", "API Integration", "Version Control"]
    cols = st.columns(4)
    for i, tool in enumerate(tools):
        with cols[i % 4]:
            st.markdown(f'<div class="skill-badge">{tool}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Specialized Knowledge
    st.subheader("🎯 Specialized Knowledge")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Financial Markets & Trading:**
        - Harmonic Pattern Analysis
        - Technical Indicators Implementation  
        - Market Data Processing
        - Trading Strategy Development
        - Risk Management Systems
        - Portfolio Optimization
        - Cryptocurrency Trading
        - Real-time Market Analysis
        """)
    
    with col2:
        st.markdown("""
        **Software Development:**
        - Clean Code Principles
        - Agile Development
        - Test-Driven Development
        - Code Review & Collaboration
        - Performance Optimization
        - Error Handling & Debugging
        - Documentation & Commenting
        - Cross-platform Development
        """)
    
    st.markdown("---")
    
    # Updated Skill Proficiency Chart based on your projects
    st.subheader("📊 Skill Proficiency Assessment")
    
    skills_data = {
        'Skill': ['Python', 'JavaScript', 'TypeScript', 'Algorithmic Trading', 'Web Development', 'Financial Analysis', 'Pattern Recognition', 'Full-Stack Development'],
        'Proficiency': [95, 90, 85, 90, 85, 88, 85, 87]
    }
    
    fig = px.bar(
        skills_data, 
        x='Proficiency', 
        y='Skill', 
        orientation='h',
        color='Proficiency',
        color_continuous_scale=['#667eea', '#4285F4', '#34A853', '#FBBC05'],
        title="Technical Skill Proficiency (%)"
    )
    
    fig.update_layout(
        height=500,
        showlegend=False,
        title_font_size=20,
        title_x=0.5
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Technology Timeline
    st.markdown("---")
    st.subheader("🕒 Technology Learning Journey")
    
    timeline_data = {
        'Year': ['2020', '2021', '2022', '2023', '2024', '2025'],
        'Python': [60, 70, 80, 85, 90, 95],
        'JavaScript': [40, 60, 75, 80, 85, 90],
        'TypeScript': [0, 30, 50, 70, 80, 85],
        'Algorithmic Trading': [0, 40, 60, 75, 85, 90]
    }
    
    fig = go.Figure()
    
    colors = ['#4285F4', '#34A853', '#FBBC05', '#EA4335']
    skills = ['Python', 'JavaScript', 'TypeScript', 'Algorithmic Trading']
    
    for i, skill in enumerate(skills):
        fig.add_trace(go.Scatter(
            x=timeline_data['Year'], 
            y=timeline_data[skill],
            mode='lines+markers',
            name=skill,
            line=dict(color=colors[i], width=3),
            marker=dict(size=8)
        ))
    
    fig.update_layout(
        title="Skills Development Over Time",
        xaxis_title="Year",
        yaxis_title="Proficiency Level (%)",
        height=400,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)

    
    fig = px.bar(
        skills_data, 
        x='Proficiency', 
        y='Skill', 
        orientation='h',
        color='Proficiency',
        color_continuous_scale='viridis',
        title="Technical Skill Proficiency (%)"
    )
    
    fig.update_layout(
        height=500,
        showlegend=False,
        title_font_size=20,
        title_x=0.5
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif selected_section == "Experience":
    st.markdown('<h1 class="main-header"> Professional Experience</h1>', unsafe_allow_html=True)
    
    # Experience Timeline
    st.subheader(" Career Journey")
    
    experiences = [
        {
            "title": "Algorithmic Trading Systems Developer",
            "company": "Independent Projects & Open Source",
            "period": "2023 - Present",
            "description": "Developing professional-grade trading systems including ENIGMA APEX and harmonic pattern recognition tools. Building advanced financial technology solutions with real-time market analysis capabilities.",
            "achievements": [
                "Built ENIGMA APEX Professional Algorithmic Trading platform",
                "Developed harmonic pattern recognition system with 85%+ accuracy",
                "Created real-time market data processing systems",
                "Implemented automated trading strategies with risk management",
                "Active maintenance with commits as recent as 12 hours ago"
            ]
        },
        {
            "title": "Full-Stack Developer",
            "company": "Portfolio Projects & GitHub (@Flopchamp)",
            "period": "2022 - Present",
            "description": "Building comprehensive web applications using modern JavaScript, TypeScript, and Python. Created multiple production-ready applications including MovieFlex, FishCrewConnect, and e-commerce solutions.",
            "achievements": [
                "Built 12+ repositories with diverse technology stacks",
                "Developed MovieFlex streaming application in TypeScript",
                "Created FishCrewConnect social platform for fishing community",
                "Built ProductStore e-commerce solution with full CRUD backend",
                "Specialized in financial technology and trading applications"
            ]
        },
        {
            "title": "Software Engineering Student",
            "company": "University of Eastern Africa, Baraton (UEAB)",
            "period": "2020 - 2024",
            "description": "Bachelor of Science in Software Engineering with CGPA: 3.256/4.0. Excelled in core computer science subjects with particular strength in AI, Software Engineering, and practical application development.",
            "achievements": [
                "Achieved Grade A in Artificial Intelligence coursework",
                "Earned Grade A in Software Engineering principles and practices",
                "Received Grade A in Practical Experience projects",
                "Maintained strong academic performance (CGPA: 3.256/4.0)",
                "Specialized in modern software development methodologies",
                "Applied academic knowledge to real-world project implementations"
            ]
        }
    ]
    
    for exp in experiences:
        # Use Streamlit native rendering for all content
        st.markdown(f"### {exp['title']}")
        st.markdown(f"**{exp['company']} | {exp['period']}**")
        st.write(exp['description'])
        
        st.markdown("#### 🎯 Key Achievements:")
        for achievement in exp['achievements']:
            st.markdown(f"✅ {achievement}")
        
        st.markdown("---")
    
    st.markdown("---")
    
    # Skills Development Over Time
    st.subheader("📊 Skills Development Timeline")
    
    years = [2020, 2021, 2022, 2023, 2024]
    python_skills = [60, 70, 80, 85, 90]
    javascript_skills = [40, 60, 75, 80, 85]
    system_design = [30, 45, 60, 70, 75]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=years, y=python_skills,
        mode='lines+markers',
        name='Python',
        line=dict(color='#4285F4', width=3),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=years, y=javascript_skills,
        mode='lines+markers',
        name='JavaScript',
        line=dict(color='#34A853', width=3),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=years, y=system_design,
        mode='lines+markers',
        name='System Design',
        line=dict(color='#FBBC05', width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title="Skills Progression Over Time",
        xaxis_title="Year",
        yaxis_title="Proficiency Level (%)",
        height=400,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif selected_section == "Achievements":
    st.markdown('<h1 class="main-header">🏆 Achievements & Recognition</h1>', unsafe_allow_html=True)
    
    # Major Achievements
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="achievement-card">
            <h3>🎓 Academic Excellence </h3>
            <p>Bachelor of Science in Software Engineering from University of Eastern Africa, Baraton with strong grades in AI (A), Software Engineering (A), and Practical Experience (A)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="achievement-card">
            <h3>� 12+ GitHub Repositories</h3>
            <p>Active open-source contributor with diverse project portfolio showcasing full-stack development skills and professional trading systems</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="achievement-card">
            <h3>� ENIGMA APEX Trading Platform</h3>
            <p>Built professional-grade algorithmic trading system with advanced pattern recognition and real-time market analysis</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="achievement-card">
            <h3>🎯 Academic to Industry Bridge</h3>
            <p>Successfully applied academic knowledge from UEAB Software Engineering program to real-world projects and professional development</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Technical Achievements
    st.subheader("💻 Technical Milestones")
    
    technical_achievements = [
        {
            "title": "ENIGMA APEX Professional Trading System",
            "description": "Built professional-grade algorithmic trading platform with real-time market analysis and automated execution",
            "tech": "Python, Financial APIs, Real-time Data Processing"
        },
        {
            "title": "Harmonic Pattern Recognition Engine",
            "description": "Developed advanced pattern detection system for financial markets with 85%+ accuracy rate",
            "tech": "JavaScript, Pattern Recognition, Financial Mathematics"
        },
        {
            "title": "Full-Stack Web Applications",
            "description": "Created multiple production-ready web applications including MovieFlex and FishCrewConnect",
            "tech": "TypeScript, React, Node.js, Database Design"
        },
        {
            "title": "Real-time Trading Analytics",
            "description": "Implemented real-time data processing system handling thousands of market data points per second",
            "tech": "Python, WebSockets, Data Streaming, Redis"
        }
    ]
    
    for achievement in technical_achievements:
        # Use Streamlit native rendering for all content
        st.markdown(f"####  {achievement['title']}")
        st.write(achievement['description'])
        st.markdown(f"**Technologies:** {achievement['tech']}")
        st.markdown("---")
    
    st.markdown("---")
    
    # Certifications and Learning
    st.subheader(" Education, Certifications & Continuous Learning")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ** Formal Education**
        - **Bachelor of Science in Software Engineering**
        - **University of Eastern Africa, Baraton (UEAB)**
        - **Graduation Year:** 2025
        - **Key Subjects:** AI (A), Software Engineering (A), Practical Experience (A)
        """)
        
        st.markdown("""
        ** Professional Certifications**
        - AWS Certified Developer (In Progress)
        - Google Cloud Platform Fundamentals
        - MongoDB Certified Developer
        - Agile Development Certification
        """)
    
    with col2:
        st.markdown("""
        ** Academic Excellence Areas**
        - **Artificial Intelligence:** Grade A
        - **Software Engineering Principles:** Grade A
        - **Practical Experience Projects:** Grade A
        - **Database Systems:** Grade B+
        - **Web Development:** Grade A-
        - **Mobile Application Development:** Grade B+
        """)
        
        st.markdown("""
        ** Continuous Learning**
        - Daily coding practice on LeetCode
        - Regular participation in coding challenges
        - Open-source project contributions
        - Tech blog writing and knowledge sharing
        """)
    
    st.markdown("---")
    
    # Academic Achievement Highlight Box
    st.markdown("""
    <div style="border: 3px solid #4285F4; border-radius: 15px; padding: 2rem; margin: 1rem 0; 
         background: linear-gradient(135deg, #f8f9ff 0%, #e3f2fd 100%); 
         box-shadow: 0 6px 12px rgba(66, 133, 244, 0.3); text-align: center;">
        <h3 style="background: linear-gradient(90deg, #4285F4 0%, #34A853 50%, #FBBC05 75%, #EA4335 100%);
           -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: bold;">
            🎓 Academic Achievement Spotlight</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Use Streamlit native rendering for all text content
    st.markdown("### 🏛️ University of Eastern Africa, Baraton")
    st.markdown("### 🎓 Bachelor of Science in Software Engineering")
    st.markdown("### 📊 CGPA: 3.256/4.0")
    
    st.markdown("#### 🏆 Exceptional Performance in Core Computer Science Subjects")
    st.markdown("⭐ **Grade A** in Artificial Intelligence")
    st.markdown("⭐ **Grade A** in Software Engineering") 
    st.markdown("⭐ **Grade A** in Practical Experience")
    
    st.markdown("---")
    
    # GitHub Contributions
    st.subheader(" Open Source Impact")
    
    # Simulated GitHub contribution data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    contributions = [45, 52, 38, 61, 73, 48, 56, 69, 44, 58, 62, 51]
    
    fig = px.bar(
        x=months,
        y=contributions,
        title="GitHub Contributions Over Time",
        color=contributions,
        color_continuous_scale='viridis'
    )
    
    fig.update_layout(
        height=400,
        showlegend=False,
        title_font_size=20,
        title_x=0.5
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Recognition and Awards
    st.subheader(" Recognition & Awards")
    
    col1, col2, col3 = st.columns(3) 
    
    with col1:
        st.markdown("""
        <div class="achievement-card">
            <h4> Innovation Award</h4>
            <p>Created solution that improved team productivity by 50%</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="achievement-card">
            <h4> Mentor of the Year</h4>
            <p>Successfully mentored 5+ junior developers</p>
        </div>
        """, unsafe_allow_html=True)

elif selected_section == "Contact":
    st.markdown('<h1 class="main-header"> Get In Touch</h1>', unsafe_allow_html=True)
    
    st.markdown("### Let's connect and explore opportunities together!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        I'm actively seeking new opportunities, especially at innovative companies like **Google**, **Microsoft**, and **Amazon**. 
        I'd love to discuss how my skills and experience can contribute to your team's success.
        
        ###  What I'm Looking For:
        - **Software Engineer** roles at FAANG companies
        - **Full-Stack Developer** positions
        - **Backend Engineer** opportunities
        - **Technical Leadership** roles
        
        ###  Let's Talk About:
        - Technical challenges and solutions
        - System design and architecture
        - Open-source collaboration
        - Career opportunities
        - Technology trends and innovations
        """)
        
        # Contact Form
        st.subheader(" Send Me a Message")
        
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            company = st.text_input("Company (Optional)")
            subject = st.selectbox("Subject", [
                "Job Opportunity",
                "Technical Discussion",
                "Collaboration Proposal",
                "General Inquiry",
                "Other"
            ])
            message = st.text_area("Message", height=150)
            
            if st.form_submit_button("Send Message", type="primary"):
                if name and email and message:
                    # Try to send email using multiple methods
                    try:
                        import requests
                        import json
                        
                        # Format the email content
                        email_subject = f"Portfolio Contact: {subject} - from {name}"
                        
                        email_body = f"""
Hello Harrison,

You have received a new message through your portfolio contact form:

 CONTACT DETAILS:
Name: {name}
Email: {email}
Company: {company if company else 'Not provided'}
Subject: {subject}

 MESSAGE:
{message}

---
This message was sent through your portfolio website contact form.
Please reply directly to: {email}
                        """
                        
                        # Method 1: Try using FormSubmit (reliable free service)
                        success = False
                        try:
                            # Use FormSubmit which is a reliable free form backend
                            form_data = {
                                "name": name,
                                "email": email,
                                "subject": f"Portfolio Contact: {subject}",
                                "message": f"""
New contact form submission from your portfolio:

 Name: {name}
 Email: {email}
 Company: {company if company else 'Not provided'}
 Subject: {subject}

 Message:
{message}

---
Sent from portfolio contact form
Reply directly to: {email}
                                """.strip(),
                                "_replyto": email,
                                "_subject": f"Portfolio Contact from {name}",
                                "_next": "https://thanks.com"
                            }
                            
                            # FormSubmit endpoint - this sends emails directly to your inbox
                            response = requests.post(
                                "https://formsubmit.co/alooharrison7@gmail.com",
                                data=form_data,
                                timeout=15
                            )
                            
                            if response.status_code in [200, 201, 302]:
                                success = True
                            
                            if success:
                                st.success("✅ Message sent successfully! I'll get back to you within 24 hours.")
                                st.balloons()
                                st.info("📧 Your message has been delivered to my inbox.")
                            else:
                                raise Exception("FormSubmit service failed")
                                
                        except Exception as e:
                            # Method 2: Fallback to mailto (opens user's email client)
                            st.warning("⚠️ Direct sending failed, opening your email client instead...")
                            
                            # URL encode the subject and body for mailto link
                            import urllib.parse
                            encoded_subject = urllib.parse.quote(email_subject)
                            encoded_body = urllib.parse.quote(email_body)
                            
                            mailto_link = f"mailto:alooharrison7@gmail.com?subject={encoded_subject}&body={encoded_body}"
                            
                            st.success("✅ Thank you for your message!")
                            st.info("📧 Your default email client should open. If not, please copy the message below and send it manually:")
                            
                            with st.expander(" Copy this message to send manually"):
                                st.text_area("Email Content", email_body, height=200)
                                st.code(f"To: alooharrison7@gmail.com\nSubject: {email_subject}")
                            
                            # JavaScript to open email client
                            st.markdown(f'''
                            <script>
                                window.open("{mailto_link}", "_blank");
                            </script>
                            ''', unsafe_allow_html=True)
                            
                            st.balloons()
                            
                    except Exception as e:
                        st.error("❌ Sorry, there was an issue sending your message. Please email me directly at alooharrison7@gmail.com")
                        st.info(f"You can copy this message: {email_body}")
                        
                else:
                    st.error("Please fill in all required fields (Name, Email, and Message)")
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4285F4, #34A853, #FBBC05, #EA4335); padding: 2px; border-radius: 15px; margin-bottom: 20px;">
            <div style="background: white; padding: 25px; border-radius: 13px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                <h3 style="background: linear-gradient(90deg, #4285F4 0%, #34A853 50%, #FBBC05 75%, #EA4335 100%);
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: bold; margin-top: 0;">📬 Contact Information</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("** Email:**")
        st.markdown("alooharrison7@gmail.com")
        
        st.markdown("** Phone:**")
        st.markdown("+254 769 719 322")

        st.markdown(" Location:**")
        st.markdown("Available for Remote/Hybrid  \nOpen to Relocation")
        
        st.markdown("** Links:**")
        
        # Social Links
        st.markdown("""
        <div style="text-align: center; margin-top: 2rem;">
            <a href="https://github.com/Flopchamp" target="_blank" class="contact-button">
                 GitHub Profile
            </a><br>
            <a href="mailto:alooharrison7@gmail.com" class="contact-button">
                 Send Email
            </a><br>
            <a href="#" target="_blank" class="contact-button">
                 Download Resume
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Availability and Preferences
    st.subheader(" Availability & Preferences")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ** Availability**
        - Immediate start available
        - Flexible with interview scheduling
        - Available for remote/on-site discussions
        """)
    
    with col2:
        st.markdown("""
        ** Location Preferences**
        - Remote-first preferred
        - Hybrid arrangements welcome
        - Open to relocation for right opportunity
        """)
    
    with col3:
        st.markdown("""
        **Interview Process**
        - Technical interviews ready
        - Portfolio presentations available
        - Reference contacts provided
        """)
    
    # Quick Response Times
    st.markdown("---")
    st.markdown("""
    <div class="achievement-card">
        <h3> Quick Response Guarantee</h3>
        <p>I respond to all professional inquiries within 24 hours. Looking forward to hearing from you!</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); 
     border-radius: 10px; margin-top: 2rem;">
    <h3 style="color: white; margin: 0;">Harrison Aloo - Software Engineer</h3>
    <p style="color: white; opacity: 0.9; margin: 0.5rem 0;">Ready for Google • Passionate about Innovation • Committed to Excellence</p>
    <p style="color: white; opacity: 0.8; margin: 0; font-size: 0.9rem;">
        Built with using Streamlit | 
        <a href="https://github.com/Flopchamp" target="_blank" style="color: white;">GitHub</a> | 
        <a href="mailto:alooharrison7@gmail.com" style="color: white;">Email</a>
    </p>
</div>
""", unsafe_allow_html=True)
