import React from 'react';
import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';
import { FaArrowRight, FaGraduationCap, FaBook, FaChalkboardTeacher, FaUserTie, FaImages } from 'react-icons/fa';
import './Home.css';

const Home = () => {
  const [profile] = React.useState({
    name: 'Dr. Vivek Shrivastava',
    title: 'Professor & Dean',
    department: 'Department of Electrical and Electronics Engineering',
    institution: 'National Institute of Technology (NIT) Uttarakhand',
    researchInterests: [
      'Reliability Engineering',
      'System Assurance Engineering & Management',
      'Power Systems',
      'Swarm Intelligence',
      'Semiconductor & Memory Product Development'
    ]
  });

  const quickLinks = [
    { 
      icon: <FaUserTie />, 
      title: 'About & Biosketch', 
      path: '/about', 
      desc: 'Academic profile and distinguished career journey' 
    },
    { 
      icon: <FaBook />, 
      title: 'Publications', 
      path: '/publications', 
      desc: 'Scholarly articles, books, and international journals' 
    },
    { 
      icon: <FaChalkboardTeacher />, 
      title: 'Leadership & Programs', 
      path: '/projects', 
      desc: 'Administrative roles, faculty programs, and conferences' 
    },
    { 
      icon: <FaImages />, 
      title: 'Photo Gallery', 
      path: '/gallery', 
      desc: 'Visual highlights of academic and institutional events' 
    }
  ];

  // Stats are derived strictly from the provided biographical data
  const stats = [
    { number: '20+', label: 'Years Experience', path: '/about' },
    { number: '100+', label: 'Publications', path: '/publications' },
    { number: '26', label: 'Theses Supervised', path: '/about' }, // 6 Ph.D. + 20 Master's
    { number: '50+', label: 'Leadership Roles', path: '/projects' } // Based on the extensive projects/admin list
  ];

  return (
    <div className="home">
      {/* Hero Section */}
      <section className="hero">
        <div className="hero-container">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="hero-content"
          >
            <div className="hero-text">
              <h1 className="hero-title">
                {profile.name}
              </h1>
              <h2 className="hero-subtitle">
                {profile.title}
              </h2>
              <p className="hero-department">
                {profile.department}
              </p>
              <p className="hero-institution">
                {profile.institution}
              </p>  
              
              {/* Stats Section */}
              <div className="hero-stats">
                {stats.map((stat, index) => (
                  <motion.div
                    key={index}
                    initial={{ opacity: 0, scale: 0.8 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ delay: 0.5 + index * 0.1 }}
                    className="stat-wrapper"
                  >
                    <Link to={stat.path} className="stat-item">
                      <span className="stat-number">{stat.number}</span>
                      <span className="stat-label">{stat.label}</span>
                    </Link>
                  </motion.div>
                ))}
              </div>

              <div className="hero-buttons">
                <Link to="/about" className="btn btn-primary">
                  View Academic Profile
                  <FaArrowRight className="btn-icon" />
                </Link>
                <Link to="/projects" className="btn btn-primary">
                  Explore Leadership Roles
                </Link>
              </div>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Research Interests */}
      <section className="interests">
        <div className="section-container">
          <div className="section-header">
            <h2 className="section-title">Research Specializations</h2>
            <p className="section-subtitle">Areas of academic expertise and scholarly focus</p>
          </div>
          <div className="interests-grid">
            {profile.researchInterests.map((interest, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ delay: index * 0.1, duration: 0.5 }}
                className="interest-card"
              >
                <div className="interest-icon">
                  <FaGraduationCap />
                </div>
                <h3>{interest}</h3>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Quick Links */}
      <section className="quick-links">
        <div className="section-container">
          <div className="section-header">
            <h2 className="section-title">Academic Portfolio</h2>
            <p className="section-subtitle">Explore my academic contributions and professional activities</p>
          </div>
          <div className="links-grid">
            {quickLinks.map((link, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.1, duration: 0.5 }}
                className="link-wrapper"
              >
                <Link to={link.path} className="quick-link-card">
                  <div className="quick-link-icon">{link.icon}</div>
                  <h3>{link.title}</h3>
                  <p>{link.desc}</p>
                  <div className="quick-link-footer">
                    <span className="quick-link-cta">
                      Explore
                      <FaArrowRight className="quick-link-arrow" />
                    </span>
                  </div>
                </Link>
              </motion.div>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;