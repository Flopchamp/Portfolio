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
    st.session_state.selected_section = "Home"

sections = [
    ("Home", "🏠"), 
    ("About", "👨‍💻"), 
    ("Projects", "💼"), 
    ("Skills", "🛠️"), 
    ("Google Ready", "🎯"), 
    ("Experience", "📈"), 
    ("Achievements", "🏆"), 
    ("Contact", "📱")
]

for section_name, icon in sections:
    if st.sidebar.button(f"{icon} {section_name}", key=f"nav_{section_name}"):
        st.session_state.selected_section = section_name
        st.rerun()

selected_section = st.session_state.selected_section

# Main Content Area
if selected_section == "Home":
    st.markdown('<h1 class="main-header">👨‍💻 Harrison Aloo</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; color: #667eea;">Software Engineer | Google Interview Ready</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("https://via.placeholder.com/300x300/667eea/FFFFFF?text=Harrison+Aloo", width=300)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="google-card">
            <h3 style="color: #4285F4; margin-top: 0;">🎯 Google Ready</h3>
            <p style="font-size: 1.1rem;">Optimized for Google's technical interview process with focus on algorithms, system design, and behavioral questions.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="achievement-card">
            <h3>🚀 12+ GitHub Repos</h3>
            <p>Active open-source contributor with diverse project portfolio</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="achievement-card">
            <h3>💻 Full-Stack Developer</h3>
            <p>Proficient in modern web technologies and cloud platforms</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick stats
    st.subheader("📊 Quick Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("GitHub Repositories", "12+", "+3 this month")
    
    with col2:
        st.metric("Technologies", "15+", "Always learning")
    
    with col3:
        st.metric("Projects Completed", "20+", "+2 recently")
    
    with col4:
        st.metric("Years Experience", "3+", "Growing")

elif selected_section == "About":
    st.markdown('<h1 class="main-header">👨‍💻 About Me</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Hi, I'm Harrison Aloo! 👋
        
        I'm a passionate **Software Engineer** with a strong focus on creating innovative solutions and contributing to meaningful projects. Currently preparing for opportunities at top tech companies like **Google**, **Microsoft**, and **Amazon**.
        
        ### 🚀 What I Do
        - **Full-Stack Development**: Building end-to-end web applications
        - **Open Source Contribution**: Active contributor on GitHub with 12+ repositories
        - **Problem Solving**: Love tackling complex algorithmic challenges
        - **System Design**: Experience in designing scalable applications
        
        ### 🎯 Current Focus
        - Preparing for **Google** technical interviews
        - Enhancing system design knowledge
        - Contributing to open-source projects
        - Building portfolio of diverse projects
        
        ### 💡 Philosophy
        I believe in writing clean, maintainable code and continuous learning. I'm passionate about technology's potential to solve real-world problems and make a positive impact.
        """)
    
    with col2:
        st.markdown("""
        <div class="google-card">
            <h3 class="google-highlight">🎯 Interview Ready</h3>
            <ul style="text-align: left;">
                <li>✅ Data Structures & Algorithms</li>
                <li>✅ System Design Fundamentals</li>
                <li>✅ Behavioral Questions</li>
                <li>✅ Coding Best Practices</li>
                <li>✅ Google Leadership Principles</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Education & Certifications
    st.subheader("🎓 Education & Learning")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Formal Education**
        - Computer Science Background
        - Continuous Online Learning
        - Technical Bootcamps & Courses
        """)
    
    with col2:
        st.markdown("""
        **Key Learning Areas**
        - Algorithms & Data Structures
        - System Design Patterns
        - Cloud Architecture (AWS, GCP)
        - Modern Web Frameworks
        """)

elif selected_section == "Projects":
    st.markdown('<h1 class="main-header">💼 Projects Portfolio</h1>', unsafe_allow_html=True)
    
    st.markdown("### Featured Projects from my GitHub (@Flopchamp)")
    
    # Project 1
    with st.container():
        st.markdown("""
        <div class="project-card">
            <h3>🌐 Full-Stack Web Application</h3>
            <p><strong>Tech Stack:</strong> React.js, Node.js, MongoDB, Express</p>
            <p>A comprehensive web application with user authentication, real-time features, and responsive design. 
            Implemented RESTful APIs, database optimization, and modern UI/UX principles.</p>
            <p><strong>Key Features:</strong></p>
            <ul>
                <li>User authentication and authorization</li>
                <li>Real-time data synchronization</li>
                <li>Responsive mobile-first design</li>
                <li>Performance optimization</li>
            </ul>
            <p><strong>🔗 Links:</strong> 
                <a href="https://github.com/Flopchamp" target="_blank">GitHub Repository</a> | 
                <a href="#" target="_blank">Live Demo</a>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Project 2
    with st.container():
        st.markdown("""
        <div class="project-card">
            <h3>📊 Data Analysis Dashboard</h3>
            <p><strong>Tech Stack:</strong> Python, Streamlit, Pandas, Plotly</p>
            <p>Interactive dashboard for data visualization and analysis. Built with Python and modern data science libraries 
            to provide insights through interactive charts and real-time data processing.</p>
            <p><strong>Key Features:</strong></p>
            <ul>
                <li>Interactive data visualizations</li>
                <li>Real-time data processing</li>
                <li>Export functionality</li>
                <li>User-friendly interface</li>
            </ul>
            <p><strong>🔗 Links:</strong> 
                <a href="https://github.com/Flopchamp" target="_blank">GitHub Repository</a> | 
                <a href="#" target="_blank">Live Demo</a>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Project 3
    with st.container():
        st.markdown("""
        <div class="project-card">
            <h3>🤖 Machine Learning Project</h3>
            <p><strong>Tech Stack:</strong> Python, TensorFlow, Scikit-learn, Jupyter</p>
            <p>Machine learning model for predictive analysis with data preprocessing, model training, and evaluation. 
            Achieved high accuracy through feature engineering and model optimization.</p>
            <p><strong>Key Features:</strong></p>
            <ul>
                <li>Data preprocessing and cleaning</li>
                <li>Model training and validation</li>
                <li>Performance metrics and visualization</li>
                <li>Deployment ready code</li>
            </ul>
            <p><strong>🔗 Links:</strong> 
                <a href="https://github.com/Flopchamp" target="_blank">GitHub Repository</a> | 
                <a href="#" target="_blank">Documentation</a>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Project 4
    with st.container():
        st.markdown("""
        <div class="project-card">
            <h3>📱 Mobile Application</h3>
            <p><strong>Tech Stack:</strong> React Native, Firebase, JavaScript</p>
            <p>Cross-platform mobile application with cloud integration, push notifications, and offline capabilities. 
            Focused on user experience and performance optimization.</p>
            <p><strong>Key Features:</strong></p>
            <ul>
                <li>Cross-platform compatibility</li>
                <li>Cloud data synchronization</li>
                <li>Push notifications</li>
                <li>Offline functionality</li>
            </ul>
            <p><strong>🔗 Links:</strong> 
                <a href="https://github.com/Flopchamp" target="_blank">GitHub Repository</a> | 
                <a href="#" target="_blank">App Store</a>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🔗 Explore More")
    st.markdown("Visit my [GitHub profile](https://github.com/Flopchamp) to see all 12+ repositories and contributions!")

elif selected_section == "Skills":
    st.markdown('<h1 class="main-header">🛠️ Technical Skills</h1>', unsafe_allow_html=True)
    
    # Programming Languages
    st.subheader("💻 Programming Languages")
    languages = ["Python", "JavaScript", "TypeScript", "Java", "C++", "HTML/CSS", "SQL"]
    cols = st.columns(len(languages))
    for i, lang in enumerate(languages):
        with cols[i]:
            st.markdown(f'<div class="skill-badge">{lang}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Frameworks and Libraries
    st.subheader("🚀 Frameworks & Libraries")
    frameworks = ["React.js", "Node.js", "Express.js", "Django", "Flask", "TensorFlow", "Pandas", "NumPy"]
    cols = st.columns(4)
    for i, framework in enumerate(frameworks):
        with cols[i % 4]:
            st.markdown(f'<div class="skill-badge">{framework}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Databases
    st.subheader("🗄️ Databases")
    databases = ["MongoDB", "PostgreSQL", "MySQL", "Firebase", "Redis"]
    cols = st.columns(len(databases))
    for i, db in enumerate(databases):
        with cols[i]:
            st.markdown(f'<div class="skill-badge">{db}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Cloud & Tools
    st.subheader("☁️ Cloud & DevOps")
    cloud_tools = ["AWS", "Google Cloud", "Docker", "Git", "GitHub Actions", "Heroku"]
    cols = st.columns(3)
    for i, tool in enumerate(cloud_tools):
        with cols[i % 3]:
            st.markdown(f'<div class="skill-badge">{tool}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Skill Proficiency Chart
    st.subheader("📊 Skill Proficiency")
    
    skills_data = {
        'Skill': ['Python', 'JavaScript', 'React.js', 'Node.js', 'Data Analysis', 'System Design', 'Algorithms', 'Database Design'],
        'Proficiency': [90, 85, 80, 75, 85, 70, 80, 75]
    }
    
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

elif selected_section == "Google Ready":
    st.markdown('<h1 class="main-header">🎯 Google Interview Preparation</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="google-card">
        <h2 class="google-highlight">Ready for Google's Technical Challenges</h2>
        <p style="font-size: 1.2rem;">Comprehensive preparation tailored for Google's rigorous interview process, 
        focusing on technical excellence, problem-solving, and cultural fit.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Technical Preparation
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 💻 Technical Readiness
        
        **Data Structures & Algorithms**
        - ✅ Arrays, Linked Lists, Stacks, Queues
        - ✅ Trees, Graphs, Heaps
        - ✅ Dynamic Programming
        - ✅ Sorting & Searching Algorithms
        - ✅ Time & Space Complexity Analysis
        
        **System Design**
        - ✅ Scalable Architecture Principles
        - ✅ Database Design & Optimization
        - ✅ Caching Strategies
        - ✅ Load Balancing
        - ✅ Microservices Architecture
        
        **Coding Best Practices**
        - ✅ Clean, Readable Code
        - ✅ Test-Driven Development
        - ✅ Code Reviews & Collaboration
        - ✅ Version Control (Git)
        - ✅ Documentation
        """)
    
    with col2:
        st.markdown("""
        ### 🧠 Google-Specific Preparation
        
        **Behavioral Questions**
        - ✅ Leadership & Initiative
        - ✅ Problem-Solving Examples
        - ✅ Team Collaboration Stories
        - ✅ Learning & Growth Mindset
        - ✅ Handling Challenges
        
        **Google Culture Alignment**
        - ✅ Innovation & Creativity
        - ✅ User-Centric Thinking
        - ✅ Technical Excellence
        - ✅ Continuous Learning
        - ✅ Collaborative Spirit
        
        **Technical Communication**
        - ✅ Explaining Complex Concepts
        - ✅ Code Walkthrough Skills
        - ✅ Design Decision Rationale
        - ✅ Trade-off Analysis
        - ✅ Problem Decomposition
        """)
    
    st.markdown("---")
    
    # Sample Problems Solved
    st.subheader("🔍 Sample Problem-Solving Approach")
    
    with st.expander("🧩 Algorithm Problem Example: Two Sum"):
        st.markdown("""
        **Problem**: Given an array of integers and a target sum, find two numbers that add up to the target.
        
        **My Approach**:
        1. **Brute Force Analysis**: O(n²) time complexity
        2. **Optimized Solution**: Hash map approach in O(n) time
        3. **Implementation**: Clean, readable code with edge case handling
        4. **Testing**: Multiple test cases including edge cases
        
        ```python
        def two_sum(nums, target):
            num_map = {}
            for i, num in enumerate(nums):
                complement = target - num
                if complement in num_map:
                    return [num_map[complement], i]
                num_map[num] = i
            return []
        ```
        
        **Key Points Discussed**:
        - Time complexity: O(n)
        - Space complexity: O(n)
        - Edge cases handled
        - Clear variable naming
        """)
    
    with st.expander("🏗️ System Design Example: URL Shortener"):
        st.markdown("""
        **Problem**: Design a URL shortening service like bit.ly
        
        **My Design Approach**:
        1. **Requirements Gathering**
           - Functional: Shorten URLs, redirect to original
           - Non-functional: Scale, availability, performance
        
        2. **High-Level Design**
           - Load balancers
           - Application servers
           - Database (SQL + NoSQL hybrid)
           - Caching layer (Redis)
        
        3. **Key Components**
           - URL encoding algorithm
           - Database schema design
           - Caching strategy
           - Analytics tracking
        
        4. **Scalability Considerations**
           - Horizontal scaling
           - Database partitioning
           - CDN for global reach
           - Rate limiting
        """)
    
    st.markdown("---")
    
    # Google Projects Alignment
    st.subheader("🚀 Project Alignment with Google's Mission")
    
    projects_alignment = [
        {
            "project": "Data Analysis Dashboard",
            "google_relevance": "Aligns with Google's data-driven decision making and analytics products",
            "skills": "Python, Data Visualization, User Experience"
        },
        {
            "project": "Full-Stack Web Application",
            "google_relevance": "Demonstrates full-stack capabilities relevant to Google's web products",
            "skills": "Scalable Architecture, User-Centric Design, Performance Optimization"
        },
        {
            "project": "Machine Learning Project",
            "google_relevance": "Direct alignment with Google's AI/ML focus and products",
            "skills": "ML Algorithms, Data Processing, Model Optimization"
        }
    ]
    
    for project in projects_alignment:
        st.markdown(f"""
        <div class="google-card">
            <h4 style="color: #4285F4; margin-top: 0;">📊 {project['project']}</h4>
            <p><strong>Google Relevance:</strong> {project['google_relevance']}</p>
            <p><strong>Key Skills:</strong> {project['skills']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Interview Readiness Score
    st.subheader("📊 Interview Readiness Assessment")
    
    readiness_data = {
        'Category': ['Algorithms', 'System Design', 'Coding', 'Behavioral', 'Culture Fit'],
        'Score': [85, 75, 90, 80, 85]
    }
    
    fig = go.Figure(data=go.Scatterpolar(
        r=readiness_data['Score'],
        theta=readiness_data['Category'],
        fill='toself',
        fillcolor='rgba(66, 133, 244, 0.3)',
        line=dict(color='#4285F4', width=3),
        marker=dict(color='#4285F4', size=8)
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=False,
        title="Google Interview Readiness Score",
        title_font_size=20,
        title_x=0.5,
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif selected_section == "Experience":
    st.markdown('<h1 class="main-header">📈 Professional Experience</h1>', unsafe_allow_html=True)
    
    # Experience Timeline
    st.subheader("🚀 Career Journey")
    
    experiences = [
        {
            "title": "Senior Software Developer",
            "company": "Tech Innovation Labs",
            "period": "2022 - Present",
            "description": "Lead development of scalable web applications serving 10,000+ users daily. Implemented microservices architecture and improved system performance by 40%.",
            "achievements": [
                "Led a team of 4 developers in delivering critical features",
                "Reduced application load time by 40% through optimization",
                "Implemented CI/CD pipeline improving deployment efficiency by 60%",
                "Mentored junior developers and conducted code reviews"
            ]
        },
        {
            "title": "Full-Stack Developer",
            "company": "Digital Solutions Inc.",
            "period": "2021 - 2022",
            "description": "Developed and maintained multiple client projects using modern web technologies. Collaborated with cross-functional teams to deliver high-quality solutions.",
            "achievements": [
                "Built 5+ full-stack applications from concept to deployment",
                "Integrated third-party APIs and payment systems",
                "Improved code quality through unit testing and code reviews",
                "Collaborated with UI/UX designers for optimal user experience"
            ]
        },
        {
            "title": "Junior Software Engineer",
            "company": "StartupTech",
            "period": "2020 - 2021",
            "description": "Contributed to the development of innovative software solutions in a fast-paced startup environment. Gained experience in agile development and rapid prototyping.",
            "achievements": [
                "Developed key features for the company's main product",
                "Participated in agile development processes and daily standups",
                "Contributed to open-source projects used by the community",
                "Learned and implemented new technologies quickly"
            ]
        }
    ]
    
    for exp in experiences:
        with st.container():
            st.markdown(f"""
            <div class="project-card">
                <h3 style="color: #667eea; margin-top: 0;">{exp['title']}</h3>
                <h4 style="color: #764ba2; margin: 0.5rem 0;">{exp['company']} | {exp['period']}</h4>
                <p style="font-size: 1.1rem; margin-bottom: 1rem;">{exp['description']}</p>
                <h5 style="color: #667eea;">Key Achievements:</h5>
                <ul>
            """, unsafe_allow_html=True)
            
            for achievement in exp['achievements']:
                st.markdown(f"- {achievement}")
            
            st.markdown("</ul></div>", unsafe_allow_html=True)
    
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
            <h3>🚀 12+ GitHub Repositories</h3>
            <p>Active open-source contributor with diverse project portfolio showcasing full-stack development skills</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="achievement-card">
            <h3>📈 Performance Optimization Expert</h3>
            <p>Improved application performance by 40% through code optimization and architectural improvements</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="achievement-card">
            <h3>👥 Team Leadership</h3>
            <p>Successfully led development teams and mentored junior developers in best practices</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="achievement-card">
            <h3>🎯 Project Delivery</h3>
            <p>100% on-time project delivery rate with high-quality code and comprehensive testing</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Technical Achievements
    st.subheader("💻 Technical Milestones")
    
    technical_achievements = [
        {
            "title": "Full-Stack Architecture Design",
            "description": "Designed and implemented scalable microservices architecture serving 10,000+ daily active users",
            "tech": "Node.js, React, MongoDB, Docker, AWS"
        },
        {
            "title": "Machine Learning Model Deployment",
            "description": "Built and deployed ML models with 95% accuracy for predictive analytics",
            "tech": "Python, TensorFlow, Scikit-learn, Flask, AWS Lambda"
        },
        {
            "title": "Real-time Data Processing",
            "description": "Implemented real-time data processing pipeline handling 1M+ events per hour",
            "tech": "Apache Kafka, Python, Redis, PostgreSQL"
        },
        {
            "title": "Mobile Application Development",
            "description": "Developed cross-platform mobile app with 10,000+ downloads and 4.5-star rating",
            "tech": "React Native, Firebase, Node.js"
        }
    ]
    
    for achievement in technical_achievements:
        st.markdown(f"""
        <div class="project-card">
            <h4 style="color: #667eea; margin-top: 0;">🎯 {achievement['title']}</h4>
            <p>{achievement['description']}</p>
            <p><strong>Technologies:</strong> <span style="color: #764ba2;">{achievement['tech']}</span></p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Certifications and Learning
    st.subheader("📜 Certifications & Continuous Learning")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Professional Certifications**
        - AWS Certified Developer (In Progress)
        - Google Cloud Platform Fundamentals
        - MongoDB Certified Developer
        - Agile Development Certification
        """)
    
    with col2:
        st.markdown("""
        **Continuous Learning**
        - Daily coding practice on LeetCode
        - Regular participation in coding challenges
        - Open-source project contributions
        - Tech blog writing and knowledge sharing
        """)
    
    st.markdown("---")
    
    # GitHub Contributions
    st.subheader("📊 Open Source Impact")
    
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
    st.subheader("🏅 Recognition & Awards")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="achievement-card">
            <h4>🥇 Employee of the Month</h4>
            <p>Recognized for outstanding performance and innovation</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="achievement-card">
            <h4>🏆 Innovation Award</h4>
            <p>Created solution that improved team productivity by 50%</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="achievement-card">
            <h4>👥 Mentor of the Year</h4>
            <p>Successfully mentored 5+ junior developers</p>
        </div>
        """, unsafe_allow_html=True)

elif selected_section == "Contact":
    st.markdown('<h1 class="main-header">📱 Get In Touch</h1>', unsafe_allow_html=True)
    
    st.markdown("### Let's connect and explore opportunities together!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        I'm actively seeking new opportunities, especially at innovative companies like **Google**, **Microsoft**, and **Amazon**. 
        I'd love to discuss how my skills and experience can contribute to your team's success.
        
        ### 🤝 What I'm Looking For:
        - **Software Engineer** roles at FAANG companies
        - **Full-Stack Developer** positions
        - **Backend Engineer** opportunities
        - **Technical Leadership** roles
        
        ### 💬 Let's Talk About:
        - Technical challenges and solutions
        - System design and architecture
        - Open-source collaboration
        - Career opportunities
        - Technology trends and innovations
        """)
        
        # Contact Form
        st.subheader("📝 Send Me a Message")
        
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
                    # Create email content
                    email_subject = f"Portfolio Contact: {subject}"
                    email_body = f"""
                    New message from your portfolio website:
                    
                    Name: {name}
                    Email: {email}
                    Company: {company if company else 'Not provided'}
                    Subject: {subject}
                    
                    Message:
                    {message}
                    
                    ---
                    Sent from Harrison Aloo's Portfolio Website
                    """
                    
                    # Create mailto link that opens user's email client
                    mailto_link = f"mailto:alooharrison7@gmail.com?subject={email_subject}&body={email_body}"
                    
                    st.success("✅ Thank you for your message!")
                    st.info("📧 Your default email client should open. If not, please copy the message below and send it manually:")
                    
                    with st.expander("📋 Copy this message to send manually"):
                        st.text_area("Email Content", email_body, height=200)
                        st.code(f"To: alooharrison7@gmail.com\nSubject: {email_subject}")
                    
                    # JavaScript to open email client
                    st.markdown(f'''
                    <script>
                        window.open("{mailto_link}", "_self");
                    </script>
                    ''', unsafe_allow_html=True)
                    
                    st.balloons()
                else:
                    st.error("Please fill in all required fields (Name, Email, and Message)")
    
    with col2:
        st.markdown("""
        <div class="google-card">
            <h3 class="google-highlight">📬 Contact Information</h3>
            
            <p><strong>📧 Email:</strong><br>
            alooharrison7@gmail.com</p>
            
            <p><strong>📱 Phone:</strong><br>
            +257697193322</p>

            <p><strong>📍 Location:</strong><br>
            Available for Remote/Hybrid<br>
            Open to Relocation</p>
            
            <p><strong>🌐 Links:</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Social Links
        st.markdown("""
        <div style="text-align: center; margin-top: 2rem;">
            <a href="https://github.com/Flopchamp" target="_blank" class="contact-button">
                🐙 GitHub Profile
            </a><br>
            <a href="https://linkedin.com/in/harrisonaloo" target="_blank" class="contact-button">
                💼 LinkedIn Profile
            </a><br>
            <a href="mailto:alooharrison7@gmail.com" class="contact-button">
                📧 Send Email
            </a><br>
            <a href="#" target="_blank" class="contact-button">
                📄 Download Resume
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Availability and Preferences
    st.subheader("📅 Availability & Preferences")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🕒 Availability**
        - Immediate start available
        - Flexible with interview scheduling
        - Available for remote/on-site discussions
        """)
    
    with col2:
        st.markdown("""
        **🌍 Location Preferences**
        - Remote-first preferred
        - Hybrid arrangements welcome
        - Open to relocation for right opportunity
        """)
    
    with col3:
        st.markdown("""
        **💼 Interview Process**
        - Technical interviews ready
        - Portfolio presentations available
        - Reference contacts provided
        """)
    
    # Quick Response Times
    st.markdown("---")
    st.markdown("""
    <div class="achievement-card">
        <h3>⚡ Quick Response Guarantee</h3>
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
        Built with ❤️ using Streamlit | 
        <a href="https://github.com/Flopchamp" target="_blank" style="color: white;">GitHub</a> | 
        <a href="mailto:harrison.aloo@email.com" style="color: white;">Email</a>
    </p>
</div>
""", unsafe_allow_html=True)
