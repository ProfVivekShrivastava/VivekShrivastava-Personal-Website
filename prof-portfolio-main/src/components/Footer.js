import React from 'react';
import { FaEnvelope, FaMapMarkerAlt, FaMobileAlt, FaLinkedin, FaGraduationCap, FaUniversity, FaGoogle, FaOrcid } from 'react-icons/fa';
import './Footer.css';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-container">
        <div className="footer-section">
          <div className="footer-section-header">
            <FaUniversity className="section-icon" />
            <h3>Contact Information</h3>
          </div>
          <div className="footer-contact">
            <div className="contact-item">
              <FaEnvelope className="contact-icon" />
              <div>
                <p><a href="mailto:shvivek@nituk.ac.in" style={{ color: 'inherit', textDecoration: 'none' }}>shvivek@nituk.ac.in</a></p>
                <p><a href="mailto:shvivek@gmail.com" style={{ color: 'inherit', textDecoration: 'none' }}>shvivek@gmail.com</a></p>
              </div>
            </div>

            <div className="contact-item">
              <FaMobileAlt className="contact-icon" />
              <div>
                <p><a href="tel:+918800681277" style={{ color: 'inherit', textDecoration: 'none' }}>+91 8800681277</a></p>
              </div>
            </div>
            
            <div className="contact-item">
              <FaMapMarkerAlt className="contact-icon" />
              <p>Department of Electrical Engineering<br />National Institute of Technology, Uttarakhand<br />NH-58, Srinagar (Garhwal), Uttarakhand-246174, India</p>
            </div>
          </div>
        </div>

        <div className="footer-section">
          <div className="footer-section-header">
            <FaGraduationCap className="section-icon" />
            <h3>Academic Portfolio</h3>
          </div>
          <div className="footer-links">
            <a href="/about">About & Biosketch</a>
            <a href="/projects">Leadership & Programs</a>
            <a href="/publications">Publications</a>
            <a href="/gallery">Photo Gallery</a>
          </div>
        </div>

        <div className="footer-section">
          <div className="footer-section-header">
            <FaLinkedin className="section-icon" />
            <h3>Connect & Collaborate</h3>
          </div>
          <div className="footer-social">
            <a 
              href="https://www.linkedin.com/in/vivek-shrivastava-4a838a2/" 
              target="_blank" 
              rel="noopener noreferrer" 
              aria-label="LinkedIn" 
              className="social-link"
            >
              <FaLinkedin />
              <span>LinkedIn</span>
            </a>
            <a 
              href="https://scholar.google.com/citations?user=xR0COBoAAAAJ&hl=en" 
              target="_blank" 
              rel="noopener noreferrer" 
              aria-label="Google Scholar" 
              className="social-link"
            >
              <FaGoogle />
              <span>Google Scholar</span>
            </a>
            <a 
              href="https://orcid.org/0000-0003-4300-4784" 
              target="_blank" 
              rel="noopener noreferrer" 
              aria-label="ORCID" 
              className="social-link"
            >
              <FaOrcid />
              <span>ORCID</span>
            </a>
            <a 
              href="https://portfolios.nituk.ac.in/453/dr-vivek-shrivastava/personal-details" 
              target="_blank" 
              rel="noopener noreferrer" 
              aria-label="NIT UK Portal" 
              className="social-link"
            >
              <FaUniversity />
              <span>NIT Uttarakhand</span>
            </a>
          </div>
          <div className="footer-info">
            <p>For academic leadership, research collaborations, advisory, and professional inquiries.</p>
          </div>
        </div>
      </div>

      <div className="footer-bottom">
        <div className="footer-bottom-content">
          <p>&copy; {new Date().getFullYear()} Official Website of Dr. Vivek Shrivastava. All rights reserved.</p>
          <p className="footer-credits">Professor & Dean — NIT Uttarakhand</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
