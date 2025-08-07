# Harrison Aloo - Software Engineer Portfolio

A comprehensive Streamlit portfolio showcasing full-stack development skills, algorithmic trading expertise, and readiness for FAANG interviews.

## 🚀 Live Demo
[Add your deployed link here]

## 🛠️ Tech Stack
- **Frontend**: Streamlit, HTML, CSS
- **Data Visualization**: Plotly, Pandas
- **Python Libraries**: PIL, Requests
- **Styling**: Custom CSS with gradient themes

## 📋 Features
- **Interactive Navigation**: Multi-section portfolio with sidebar navigation
- **Responsive Design**: Works on desktop and mobile devices
- **Project Showcase**: Detailed project descriptions with tech stacks
- **Skills Visualization**: Interactive charts and progress bars
- **Contact Form**: Built-in contact form for recruiters
- **GitHub Integration**: Showcases your actual GitHub repositories
- **Professional Styling**: Modern gradient themes and card layouts

## 🏃‍♂️ Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation
1. Clone this repository:
```bash
git clone [your-repo-link]
cd Portfolio
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your browser and navigate to `http://localhost:8501`

## 🎯 Customization Guide

### 1. Personal Information
Update these sections in `app.py`:
- **Line 82**: Replace profile image URL
- **Line 103-117**: Update experience years and achievements
- **Line 125-135**: Customize your overview description
- **Line 148-168**: Add your educational background and location

### 2. Projects Section
Update your projects starting from **Line 200**:
- Replace project descriptions
- Add your GitHub repository links
- Include live demo links
- Add performance metrics and achievements

### 3. Skills Section
Customize your skills in **Line 300+**:
- Update programming languages and proficiency levels
- Modify frameworks and technologies
- Adjust skill badges and categories

### 4. Experience Section
Update your work experience starting from **Line 380**:
- Replace company names and positions
- Add actual dates and responsibilities
- Include key achievements and metrics

### 5. Contact Information
Update contact details starting from **Line 520**:
- Add your actual email address
- Include LinkedIn profile URL
- Add resume download link
- Include calendar scheduling link

## 📱 Sections Overview

1. **🏠 Home**: Overview with key metrics and quick introduction
2. **👨‍💻 About**: Detailed personal and professional background
3. **💼 Projects**: Showcase of your GitHub repositories and key projects
4. **🛠️ Skills**: Interactive skills visualization and technology stack
5. **📈 Experience**: Professional experience timeline and achievements
6. **🏆 Achievements**: Awards, certifications, and recognition
7. **📱 Contact**: Contact form and social media links

## 🎨 Styling Features
- **Gradient Themes**: Modern purple-blue gradient color scheme
- **Responsive Cards**: Clean card layouts for projects and achievements
- **Interactive Charts**: Plotly-powered skill proficiency charts
- **Skill Badges**: Color-coded technology badges
- **Progress Bars**: Visual skill level indicators

## 🚀 Deployment Options

### Streamlit Cloud (Free)
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy with one click

### Heroku
1. Create a `Procfile`:
```
web: sh setup.sh && streamlit run app.py
```

2. Create a `setup.sh`:
```bash
mkdir -p ~/.streamlit/
echo "[server]" > ~/.streamlit/config.toml
echo "port = $PORT" >> ~/.streamlit/config.toml
echo "enableCORS = false" >> ~/.streamlit/config.toml
echo "headless = true" >> ~/.streamlit/config.toml
```

### Other Options
- **Vercel**: Deploy using Vercel's Python runtime
- **AWS**: Use EC2 or Elastic Beanstalk
- **DigitalOcean**: Deploy on App Platform

## 🔧 Advanced Customizations

### Adding New Sections
1. Add section to sidebar navigation (Line 45)
2. Create new elif condition in main logic
3. Design your section content
4. Update navigation handling

### Integrating APIs
- **GitHub API**: Real-time repository data
- **LinkedIn API**: Professional information
- **Email Services**: Contact form functionality
- **Analytics**: Google Analytics integration

### Performance Optimization
- **Caching**: Use `@st.cache_data` for data loading
- **Images**: Optimize image sizes and formats
- **Loading**: Add loading spinners for better UX

## 🎯 FAANG Interview Focus

This portfolio is specifically designed to impress FAANG recruiters:

- **Technical Depth**: Showcases algorithmic trading and pattern recognition
- **Full-Stack Skills**: Demonstrates frontend and backend capabilities
- **System Design**: Highlights scalable architecture thinking
- **Code Quality**: Clean, well-documented, and maintainable code
- **Innovation**: Unique combination of fintech and web development

## 📊 Analytics & Tracking

Consider adding:
- Google Analytics for visitor tracking
- Contact form submissions tracking
- Project view statistics
- Skills section engagement metrics

## 🤝 Contributing

Feel free to fork this project and customize it for your own portfolio. If you make improvements, consider contributing back!

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

If you need help customizing this portfolio:
- Check the customization guide above
- Open an issue on GitHub
- Contact me directly through the portfolio

---

**Built with ❤️ for Software Engineers targeting FAANG companies**

*This portfolio template helps showcase your skills in the best light for top tech company interviews.*
