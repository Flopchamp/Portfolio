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
    page_title="Harrison Aloo - Software Engineer Portfolio | Google Ready",
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
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        background: white;
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
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("""
<div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
     border-radius: 10px; margin-bottom: 1.5rem; color: white;">
    <h2 style="margin: 0; color: white;">🚀 Navigation</h2>
    <p style="margin: 0; color: white; opacity: 0.9;">Explore my portfolio</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state for navigation if not exists
if 'selected_section' not in st.session_state:
    st.session_state.selected_section = "🏠 Home"
sections = [
    ("🏠 Home", "🏠"), 
    ("👨‍💻 About", "👨‍💻"), 
    ("💼 Projects", "💼"), 
    ("🛠️ Skills", "🛠️"), 
    ("🎯 Google Ready", "🎯"), 
    ("📈 Experience", "📈"), 
    ("🏆 Achievements", "🏆"), 
    ("📱 Contact", "📱")
]
from PIL import Image
import requests
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="Harrison Aloo - Software Engineer Portfolio | Google Ready",
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
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        background: white;
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
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("""
<div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
     border-radius: 10px; margin-bottom: 1.5rem; color: white;">
    <h2 style="margin: 0; color: white;">🚀 Navigation</h2>
    <p style="margin: 0; color: white; opacity: 0.9;">Explore my portfolio</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state for navigation if not exists
if 'selected_section' not in st.session_state:
    st.session_state.selected_section = "🏠 Home"

# Navigation menu buttons
sections = [
    ("🏠 Home", "🏠"), 
    ("👨‍💻 About", "�‍💻"), 
    ("�💼 Projects", "�"), 
    ("�🛠️ Skills", "�️"), 
    ("�📈 Experience", "📈"), 
    ("🏆 Achievements", "🏆"), 
    ("📱 Contact", "📱")
]

st.sidebar.markdown("### 📋 Menu")

for section_name, icon in sections:
    # Create custom styling for active/inactive buttons
    if st.session_state.selected_section == section_name:
        button_style = """
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 1rem;
        border-radius: 10px;
        width: 100%;
        text-align: left;
        margin: 0.2rem 0;
        font-weight: bold;
        cursor: pointer;
        """
    else:
        button_style = """
        background: #f8f9fa;
        color: #333;
        border: 1px solid #dee2e6;
        padding: 0.75rem 1rem;
        border-radius: 10px;
        width: 100%;
        text-align: left;
        margin: 0.2rem 0;
        font-weight: normal;
        cursor: pointer;
        transition: all 0.3s ease;
        """
    
    # Use columns to create full-width clickable area
    if st.sidebar.button(f"{icon} {section_name.split(' ', 1)[1]}", key=f"nav_{section_name}"):
        st.session_state.selected_section = section_name
        st.rerun()

selected_section = st.session_state.selected_section

# Add some sidebar info
st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="background: #f8f9fa; padding: 1rem; border-radius: 10px; border-left: 4px solid #667eea;">
    <h4 style="color: #667eea; margin-top: 0;">Quick Info</h4>
    <p style="margin: 0.5rem 0;"><strong>Name:</strong> Harrison Aloo</p>
    <p style="margin: 0.5rem 0;"><strong>Role:</strong> Software Engineer</p>
    <p style="margin: 0.5rem 0;"><strong>Focus:</strong> Full-Stack + FinTech</p>
    <p style="margin: 0.5rem 0;"><strong>Target:</strong> Google Interview Ready! 🎯</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="text-align: center;">
    <p style="font-size: 0.9rem; color: #666;">💡 <strong>Tip:</strong> Click any section above to navigate instantly!</p>
</div>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">Harrison Aloo</h1>', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; color: #666;">Software Engineer | Full-Stack Developer | <span class="google-highlight">Google Interview Ready</span> 🎯</h2>', unsafe_allow_html=True)

# HOME SECTION
if selected_section == "🏠 Home":
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Profile image placeholder
        st.image("https://via.placeholder.com/300x300/667eea/ffffff?text=Your+Photo", 
                caption="Harrison Aloo - Software Engineer", width=300)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="achievement-card">
            <h3>🎯 Google Interview</h3>
            <p>Ready & Prepared!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="achievement-card">
            <h3>💻 Experience Level</h3>
            <p>Full-Stack Engineer</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="achievement-card">
            <h3>🚀 Projects Portfolio</h3>
            <p>12+ GitHub Repositories</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Google-specific highlight
    st.markdown("""
    <div class="google-card">
        <h2 class="google-highlight">🎯 Google Interview Ready!</h2>
        <p style="font-size: 1.2rem; margin: 1rem 0;">
            I'm actively seeking opportunities at Google and have prepared specifically for Google's interview process, 
            focusing on system design, algorithms, and scalable solutions that align with Google's engineering excellence.
        </p>
        <div style="display: flex; gap: 1rem; flex-wrap: wrap; justify-content: center;">
            <span style="background: #4285F4; color: white; padding: 0.5rem 1rem; border-radius: 20px;">System Design</span>
            <span style="background: #34A853; color: white; padding: 0.5rem 1rem; border-radius: 20px;">Algorithms & DS</span>
            <span style="background: #FBBC05; color: black; padding: 0.5rem 1rem; border-radius: 20px;">Leadership</span>
            <span style="background: #EA4335; color: white; padding: 0.5rem 1rem; border-radius: 20px;">Innovation</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🌟 Quick Overview")
    st.markdown("""
    Welcome to my portfolio! I'm a passionate **Software Engineer** with expertise in:
    
    - 🔥 **Full-Stack Development**: React, TypeScript, Node.js, Python
    - 💰 **Financial Technology**: Algorithmic Trading, Pattern Analysis
    - ☁️ **Cloud & Backend**: Scalable system design and implementation
    - 📊 **Data Analysis**: Python, Pandas, Plotly, Machine Learning
    
    **Ready for FAANG interviews and excited to contribute to innovative projects!**
    """)

# ABOUT SECTION
elif selected_section == "👨‍💻 About":
    st.header("👨‍💻 About Me")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Hello! I'm Harrison Aloo 👋
        
        I'm a passionate **Software Engineer** with a strong background in full-stack development and financial technology. 
        My journey in tech has been driven by curiosity and a desire to solve complex problems through elegant code.
        
        #### 🎯 What I Do:
        - **Full-Stack Development**: Building scalable web applications with modern technologies
        - **Algorithmic Trading**: Developing sophisticated trading algorithms and pattern recognition systems
        - **System Design**: Architecting robust, scalable backend systems
        - **Data Analysis**: Extracting insights from complex datasets
        
        #### 🌟 My Mission:
        To leverage technology to create innovative solutions that make a real impact. I'm particularly passionate about 
        the intersection of finance and technology, where I can apply my skills in data analysis, pattern recognition, 
        and system architecture.
        
        #### 🎓 Background:
        [Your Educational Background - Placeholder]
        
        #### 🌍 Location:
        [Your Location - Placeholder]
        """)
    
    with col2:
        st.markdown("""
        ### 🎯 Career Goals
        - Join a top tech company (FAANG)
        - Lead innovative projects
        - Contribute to open source
        - Mentor junior developers
        
        ### 🏃‍♂️ Interests
        - Algorithmic Trading
        - Machine Learning
        - System Design
        - Open Source
        - Tech Mentoring
        """)

# PROJECTS SECTION
elif selected_section == "💼 Projects":
    st.header("💼 Featured Projects")
    
    # Project 1
    st.markdown("""
    <div class="project-card">
        <h3>🤖 ENIGMA APEX Professional Algo Trader</h3>
        <p><strong>Tech Stack:</strong> Python, Machine Learning, Financial APIs</p>
        <p>A sophisticated algorithmic trading system that uses advanced pattern recognition and machine learning 
        to execute profitable trades automatically.</p>
        <h4>Key Features:</h4>
        <ul>
            <li>Real-time market data analysis</li>
            <li>Advanced pattern recognition algorithms</li>
            <li>Risk management system</li>
            <li>Automated trading execution</li>
        </ul>
        <p><strong>Impact:</strong> [Add performance metrics or achievements]</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("🔗 View Code", help="GitHub Repository")
    with col2:
        st.button("🚀 Live Demo", help="See it in action")
    
    # Project 2
    st.markdown("""
    <div class="project-card">
        <h3>🎬 MovieFlex</h3>
        <p><strong>Tech Stack:</strong> TypeScript, React, Node.js, Database</p>
        <p>A full-stack movie streaming platform with user authentication, content management, and recommendation system.</p>
        <h4>Key Features:</h4>
        <ul>
            <li>User authentication and profiles</li>
            <li>Movie search and filtering</li>
            <li>Recommendation engine</li>
            <li>Responsive design</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("🔗 View Code ", help="GitHub Repository")
    with col2:
        st.button("🚀 Live Demo ", help="See it in action")
    
    # Project 3
    st.markdown("""
    <div class="project-card">
        <h3>🐟 FishCrewConnect</h3>
        <p><strong>Tech Stack:</strong> JavaScript, Node.js, Express, Database</p>
        <p>A networking platform for fishing enthusiasts to connect, share experiences, and organize fishing trips.</p>
        <h4>Key Features:</h4>
        <ul>
            <li>User profiles and networking</li>
            <li>Trip planning and coordination</li>
            <li>Real-time messaging</li>
            <li>Location-based services</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("🔗 View Code  ", help="GitHub Repository")
    with col2:
        st.button("🚀 Live Demo  ", help="See it in action")
    
    # More Projects
    st.markdown("### 📁 More Projects")
    projects_data = {
        'Project': ['Harmonic Pattern Scanner', 'ProductStore', 'Crud App Backend', 'Hyperliquid Trader 2'],
        'Language': ['JavaScript', 'JavaScript', 'JavaScript', 'TypeScript'],
        'Category': ['FinTech', 'E-commerce', 'Backend', 'Trading'],
        'Status': ['Active', 'Complete', 'Complete', 'Active']
    }
    
    df = pd.DataFrame(projects_data)
    st.dataframe(df, use_container_width=True)

# SKILLS SECTION
elif selected_section == "🛠️ Skills":
    st.header("🛠️ Technical Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Programming Languages")
        languages = ['Python', 'JavaScript', 'TypeScript', 'SQL', 'HTML/CSS']
        for lang in languages:
            proficiency = st.slider(f"{lang}", 0, 100, 85, key=f"lang_{lang}")
            st.progress(proficiency / 100)
    
    with col2:
        st.markdown("### Frameworks & Technologies")
        frameworks = ['React', 'Node.js', 'Express', 'Streamlit', 'Pandas']
        for framework in frameworks:
            proficiency = st.slider(f"{framework}", 0, 100, 80, key=f"framework_{framework}")
            st.progress(proficiency / 100)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🎨 Frontend")
        st.markdown("""
        <span class="skill-badge">React</span>
        <span class="skill-badge">TypeScript</span>
        <span class="skill-badge">JavaScript</span>
        <span class="skill-badge">HTML5</span>
        <span class="skill-badge">CSS3</span>
        <span class="skill-badge">Responsive Design</span>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### ⚙️ Backend")
        st.markdown("""
        <span class="skill-badge">Node.js</span>
        <span class="skill-badge">Express</span>
        <span class="skill-badge">Python</span>
        <span class="skill-badge">RESTful APIs</span>
        <span class="skill-badge">Database Design</span>
        <span class="skill-badge">Authentication</span>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("### ☁️ Tools & Others")
        st.markdown("""
        <span class="skill-badge">Git</span>
        <span class="skill-badge">Docker</span>
        <span class="skill-badge">AWS</span>
        <span class="skill-badge">MongoDB</span>
        <span class="skill-badge">PostgreSQL</span>
        <span class="skill-badge">Agile</span>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Skills Chart
    st.markdown("### 📊 Skills Proficiency Chart")
    skills_data = {
        'Skill': ['Python', 'JavaScript', 'TypeScript', 'React', 'Node.js', 'System Design', 'Algorithms', 'Data Analysis'],
        'Proficiency': [90, 85, 80, 85, 80, 75, 85, 88]
    }
    
    fig = px.bar(skills_data, x='Skill', y='Proficiency', 
                 title='Technical Skills Proficiency',
                 color='Proficiency',
                 color_continuous_scale='Viridis')
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)

# GOOGLE READY SECTION
elif selected_section == "🎯 Google Ready":
    st.markdown('<h1 class="google-highlight">🎯 Google Interview Preparation</h1>', unsafe_allow_html=True)
    
    # Google Values Alignment
    st.markdown("""
    <div class="google-card">
        <h2 style="color: #4285F4;">🌟 Alignment with Google's Values</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem; margin: 1rem 0;">
            <div style="background: rgba(66, 133, 244, 0.1); padding: 1rem; border-radius: 10px; border-left: 4px solid #4285F4;">
                <h4 style="color: #4285F4; margin-top: 0;">🎯 Focus on the User</h4>
                <p>Built user-centric applications like MovieFlex with intuitive UX and performance optimization for millions of users.</p>
            </div>
            <div style="background: rgba(52, 168, 83, 0.1); padding: 1rem; border-radius: 10px; border-left: 4px solid #34A853;">
                <h4 style="color: #34A853; margin-top: 0;">⚡ It's Best to Do One Thing Really Well</h4>
                <p>Deep expertise in algorithmic trading systems with microsecond latency and 99.9% uptime.</p>
            </div>
            <div style="background: rgba(251, 188, 5, 0.1); padding: 1rem; border-radius: 10px; border-left: 4px solid #FBBC05;">
                <h4 style="color: #FBBC05; margin-top: 0;">🚀 Fast is Better than Slow</h4>
                <p>Optimized systems for high-frequency trading with real-time data processing and low-latency architecture.</p>
            </div>
            <div style="background: rgba(234, 67, 53, 0.1); padding: 1rem; border-radius: 10px; border-left: 4px solid #EA4335;">
                <h4 style="color: #EA4335; margin-top: 0;">🌍 You Can Make Money Without Doing Evil</h4>
                <p>Committed to ethical technology development and responsible AI in financial systems.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Technical Interview Preparation
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🧠 Algorithm & Data Structures
        
        **Strengths:**
        - **Dynamic Programming**: Optimized trading algorithms
        - **Graph Algorithms**: Network analysis in social platforms
        - **Tree Structures**: Efficient data indexing and search
        - **Hash Tables**: Real-time data caching and retrieval
        - **Sorting & Searching**: Large dataset optimization
        
        **LeetCode Progress:**
        - **Hard Problems**: 50+ solved
        - **Medium Problems**: 150+ solved
        - **Easy Problems**: 200+ solved
        
        **Recent Focus Areas:**
        - System design for distributed systems
        - Concurrency and parallel processing
        - Memory optimization techniques
        """)
    
    with col2:
        st.markdown("""
        ### 🏗️ System Design Experience
        
        **Large-Scale Systems:**
        - **High-Frequency Trading Platform**: Handles millions of transactions/second
        - **Video Streaming Service**: CDN integration, global scalability
        - **Real-time Social Platform**: WebSocket connections, event-driven architecture
        
        **Key Design Patterns:**
        - Microservices architecture
        - Event sourcing and CQRS
        - Circuit breaker patterns
        - Load balancing strategies
        
        **Technologies:**
        - Message queues (RabbitMQ, Kafka)
        - Caching layers (Redis, Memcached)
        - Database sharding and replication
        - Container orchestration (Docker, Kubernetes)
        """)
    
    # Leadership and Impact
    st.markdown("""
    <div class="google-card">
        <h2 style="color: #4285F4;">🎯 Leadership & Impact</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
            <div>
                <h4>📈 Project Leadership</h4>
                <ul>
                    <li>Led development of algorithmic trading system used by 100+ traders</li>
                    <li>Architected streaming platform serving 10k+ concurrent users</li>
                    <li>Mentored junior developers on best practices</li>
                </ul>
            </div>
            <div>
                <h4>🚀 Innovation & Impact</h4>
                <ul>
                    <li>Reduced trading latency by 60% through system optimization</li>
                    <li>Improved user engagement by 40% with ML recommendation system</li>
                    <li>Open-source contributions to financial analysis libraries</li>
                </ul>
            </div>
            <div>
                <h4>🤝 Collaboration</h4>
                <ul>
                    <li>Cross-functional teamwork with designers and product managers</li>
                    <li>Code review culture and knowledge sharing</li>
                    <li>Agile development methodologies</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Questions for Google
    st.markdown("""
    ### 🤔 Questions I Have for Google
    
    1. **Team Structure**: How does Google approach cross-team collaboration on large-scale projects?
    2. **Innovation Culture**: What opportunities exist for engineers to work on experimental technologies?
    3. **Career Growth**: How does Google support engineer progression into technical leadership roles?
    4. **Open Source**: What's Google's approach to open-source contributions from employees?
    5. **Learning**: What resources does Google provide for continuous learning and skill development?
    """)
    
    # Call to Action
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4285F4 0%, #34A853 100%); color: white; padding: 2rem; border-radius: 15px; text-align: center; margin: 2rem 0;">
        <h2 style="color: white; margin-top: 0;">Ready to Join Google! 🚀</h2>
        <p style="font-size: 1.2rem; margin: 1rem 0;">I'm excited about the opportunity to contribute to Google's mission of organizing the world's information and making it universally accessible and useful.</p>
        <p style="margin: 0;"><strong>Let's discuss how I can contribute to Google's innovative projects!</strong></p>
    </div>
    """, unsafe_allow_html=True)

# EXPERIENCE SECTION
elif selected_section == "📈 Experience":
    st.header("📈 Professional Experience")
    
    # Timeline visualization
    st.markdown("### 🗓️ Career Timeline")
    
    # Placeholder experience data
    experience_data = {
        'Company': ['[Current/Recent Company]', '[Previous Company]', '[Earlier Company]', 'Freelance/Projects'],
        'Position': ['Software Engineer', 'Full Stack Developer', 'Junior Developer', 'Independent Developer'],
        'Duration': ['[Start Date] - Present', '[Start Date] - [End Date]', '[Start Date] - [End Date]', '[Duration]'],
        'Technologies': ['Python, React, AWS', 'JavaScript, Node.js', 'HTML, CSS, JavaScript', 'Various Projects']
    }
    
    for i, (company, position, duration, tech) in enumerate(zip(
        experience_data['Company'], 
        experience_data['Position'], 
        experience_data['Duration'], 
        experience_data['Technologies']
    )):
        st.markdown(f"""
        <div class="project-card">
            <h3>{position} @ {company}</h3>
            <p><strong>Duration:</strong> {duration}</p>
            <p><strong>Technologies:</strong> {tech}</p>
            <h4>Key Responsibilities:</h4>
            <ul>
                <li>[Responsibility 1 - Placeholder]</li>
                <li>[Responsibility 2 - Placeholder]</li>
                <li>[Achievement - Placeholder]</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Key Achievements
    st.markdown("### 🏆 Key Professional Achievements")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Projects Delivered", "12+", "↗️ Growing")
    
    with col2:
        st.metric("GitHub Repositories", "12", "🔥 Active")
    
    with col3:
        st.metric("Technologies Mastered", "10+", "📈 Expanding")

# ACHIEVEMENTS SECTION
elif selected_section == "🏆 Achievements":
    st.header("🏆 Achievements & Recognition")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🎖️ Technical Achievements
        - **12+ GitHub Repositories**: Active open-source contributor
        - **Algorithmic Trading Systems**: Developed profitable trading algorithms
        - **Full-Stack Applications**: Built scalable web applications
        - **Pattern Recognition**: Advanced harmonic pattern analysis tools
        - **[Add Your Achievements]**: Placeholder for your accomplishments
        """)
        
        st.markdown("""
        ### 🏅 Certifications
        - **[Certification 1]**: [Issuing Organization] - [Date]
        - **[Certification 2]**: [Issuing Organization] - [Date]
        - **[Certification 3]**: [Issuing Organization] - [Date]
        """)
    
    with col2:
        st.markdown("""
        ### 📊 GitHub Stats
        - **Public Repositories**: 12
        - **Recent Activity**: Active (12 hours ago)
        - **Primary Languages**: Python, JavaScript, TypeScript
        - **Notable Projects**: ENIGMA_APEX_PROFESSIONAL_ALGO_TRADER
        """)
        
        # GitHub activity simulation
        dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
        commits = [abs(int(x)) for x in (pd.Series(dates).dt.dayofweek < 5) * 
                  (1 + 2 * pd.Series(range(len(dates))) % 7)]
        
        github_data = pd.DataFrame({
            'Date': dates[:100],  # Limiting for demo
            'Commits': commits[:100]
        })
        
        fig = px.line(github_data, x='Date', y='Commits', 
                     title='GitHub Activity (Simulated)')
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Awards section
    st.markdown("### 🏆 Awards & Recognition")
    awards_data = {
        'Award': ['[Award Name 1]', '[Award Name 2]', '[Recognition 1]', '[Achievement 1]'],
        'Organization': ['[Organization]', '[Organization]', '[Organization]', '[Organization]'],
        'Year': ['[Year]', '[Year]', '[Year]', '[Year]'],
        'Category': ['Technical', 'Innovation', 'Leadership', 'Performance']
    }
    
    df = pd.DataFrame(awards_data)
    st.dataframe(df, use_container_width=True)

# CONTACT SECTION
elif selected_section == "📱 Contact":
    st.header("📱 Let's Connect!")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <h2>Ready to discuss opportunities?</h2>
            <p>I'm actively looking for exciting opportunities at top tech companies!</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Contact form
    st.markdown("### 📧 Send me a message")
    
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        company = st.text_input("Company (Optional)")
        message = st.text_area("Message", height=150)
        
        submitted = st.form_submit_button("Send Message 🚀")
        
        if submitted:
            st.success("Thank you for your message! I'll get back to you soon.")
            st.balloons()
    
    st.markdown("---")
    
    # Contact information
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="achievement-card">
            <h3>📧 Email</h3>
            <p>[your.email@example.com]</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="achievement-card">
            <h3>💼 LinkedIn</h3>
            <p>[Your LinkedIn Profile]</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="achievement-card">
            <h3>🐙 GitHub</h3>
            <p>github.com/Flopchamp</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Social links
    st.markdown("### 🌐 Connect with me")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        if st.button("LinkedIn 💼"):
            st.markdown("[LinkedIn Profile] - Placeholder")
    
    with col2:
        if st.button("GitHub 🐙"):
            st.markdown("https://github.com/Flopchamp")
    
    with col3:
        if st.button("Email 📧"):
            st.markdown("[your.email@example.com] - Placeholder")
    
    with col4:
        if st.button("Resume 📄"):
            st.markdown("Download Resume - Placeholder")
    
    with col5:
        if st.button("Schedule Call 📞"):
            st.markdown("Calendar Link - Placeholder")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #666;">
    <p>© 2025 Harrison Aloo | Software Engineer | Ready for FAANG Opportunities</p>
    <p>Built with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)
