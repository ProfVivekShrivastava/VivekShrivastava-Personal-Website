import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { FaEnvelope, FaMapMarkerAlt, FaGraduationCap, FaGoogle, FaLinkedin, FaUserTie, FaGlobe, FaPhone, FaUniversity } from 'react-icons/fa';
import './About.css';

// Import your profile image - adjust the path according to your project structure
import profileImage from '../assets/images/pfp.jpg';

const About = () => {
  const [profile] = useState({
    name: 'Dr. Vivek Shrivastava',
    title: 'Professor & Dean',
    department: 'Department of Electrical Engineering',
    institution: 'National Institute of Technology (NIT) Uttarakhand',
    email: 'shvivek@nituk.ac.in',
    phone: '8800681277',
    address: 'Department of Electrical Engineering, National Institute of Technology, Uttarakhand, NH-58, Srinagar (Garhwal), Uttarakhand-246174, India',
    bio: 'Dr. Vivek Shrivastava possesses over two decades of diverse experience, spanning teaching, research, industry, and academic leadership roles in India, China, and the United States. Currently, he holds the position of Professor & Dean in the Department of Electrical and Electronics Engineering at the National Institute of Technology (NIT) Uttarakhand. Previously, he served at NIT Delhi for approximately seven years, assuming leadership positions such as Registrar, Dean (Research and Consultancy), Dean (Student Welfare), Dean (Faculty Welfare), and Head of the Department of Electrical Engineering. During his tenure, he fostered collaborations with industry and government organizations, contributing substantially to the institution’s growth. Dr. Shrivastava played a pivotal role in the development and implementation of the Five-Year Integrated B.Tech-M.Tech Programme (Electrical Engineering) and the Master’s program in Power Systems at Gautam Buddha University, Greater Noida. He also holds extensive experience in academic administration, having served as Faculty In-charge for Training and Placement, Library, and Nodal Officer for various projects, including TEQIP-III and RUSA. His contributions extend to committees affiliated with organizations such as AICTE and UGC. Prior to his academic career, Dr. Shrivastava held the position of System Reliability Engineer at SanDisk Semiconductors in Shanghai, China, and the United States. His contributions at SanDisk significantly contributed to the design and development of memory products. In research and consultancy, Dr. Shrivastava has secured substantial funding for projects from esteemed organizations such as the Ministry of Human Resource Development (Government of India) and the Board of Research in Nuclear Sciences (BRNS), a subsidiary of the Bhabha Atomic Research Centre. His scholarly contributions include over 100 journal articles, conference papers, and book chapters. Additionally, he has supervised six Ph.D. and 20 Master’s students, with several ongoing Ph.D. supervisions. Dr. Shrivastava holds the positions of Editor/Associate Editor for the International Journal of Swarm Intelligence (IJSI) and the International Journal of System Assurance Engineering and Management. He is a Fellow of the Institution of Engineers (India) and a Senior Member of the Institute of Electrical and Electronics Engineers (IEEE).',
    researchInterests: [
      'Reliability Engineering',
      'System Assurance Engineering and Management',
      'Swarm Intelligence',
      'Power Systems',
      'Semiconductor and Memory Product Development'
    ],
    administrativeRoles: [
      'Registrar, National Institute of Technology Delhi',
      'Dean (Research and Consultancy), NIT Delhi',
      'Dean (Student Welfare), NIT Delhi',
      'Dean (Faculty Welfare), NIT Delhi',
      'Head of the Department of Electrical Engineering, NIT Delhi',
      'Faculty In-charge for Training and Placement, Library',
      'Nodal Officer for TEQIP-III and RUSA projects',
      'Committee Member for organizations such as AICTE and UGC',
      'Editor/Associate Editor, International Journal of Swarm Intelligence (IJSI)',
      'Editor/Associate Editor, International Journal of System Assurance Engineering and Management'
    ],
    professionalMemberships: [
      'Fellow of the Institution of Engineers (India)',
      'Senior Member of the Institute of Electrical and Electronics Engineers (IEEE)'
    ],
    awards: [
      'Secured substantial funding from Ministry of Human Resource Development (Government of India)',
      'Secured project funding from Board of Research in Nuclear Sciences (BRNS, BARC)',
      'Authored over 100 journal articles, conference papers, and book chapters',
      'Supervised 6 Ph.D. and 20 Master’s students'
    ]
  });

  const [careerPositions] = useState([
    {
      role: 'Professor & Dean',
      organization: 'Department of Electrical Engineering, National Institute of Technology, Uttarakhand Srinagar',
      period: '2024 - Present'
    },
    {
      role: 'Associate Professor',
      organization: 'Department of Electrical Engineering, National Institute of Technology Delhi',
      period: '2018 - 2024'
    },
    {
      role: 'Associate Professor',
      organization: 'Department of Electrical Engineering, Rajasthan Technical University Kota',
      period: '2013 - 2018'
    },
    {
      role: 'Associate Professor',
      organization: 'Department of Electrical Engineering, National Institute of Technology Delhi',
      period: '2012 - 2013'
    },
    {
      role: 'Assistant Professor',
      organization: 'Gautam Buddha University, Greater Noida',
      period: '2010 - 2012'
    },
    {
      role: 'System Reliability Engineer',
      organization: 'SanDisk Semiconductors Shanghai, China / Milpitas California USA',
      period: '2008 - 2009'
    },
    {
      role: 'Senior Research Fellow',
      organization: 'Sponsored Research & Industrial Consultancy, IIT Kharagpur',
      period: '2005 - 2006'
    },
    {
      role: 'Junior Research Fellow',
      organization: 'Sponsored Research & Industrial Consultancy, IIT Kharagpur',
      period: '2003 - 2005'
    }
  ]);

  const [education] = useState([
    {
      _id: '1',
      degree: 'Certificate',
      field: 'Human Rights',
      institution: 'Vardhman Mahaveer Open University Kota',
      year: '2014'
    },
    {
      _id: '2',
      degree: 'Ph.D.',
      field: 'Ph.D. in Reliability Engineering',
      institution: 'Indian Institute of Technology Kharagpur, West Bengal, India',
      year: '2009'
    },
    {
      _id: '3',
      degree: 'P. G. Diploma',
      field: 'P. G. Diploma in VLSI Design',
      institution: 'BIT Mapper Pune Maharashtra',
      year: '2002'
    },
    {
      _id: '4',
      degree: 'Bachelor of Engineering',
      field: 'Electrical Engineering',
      institution: 'R. G. P. V. Bhopal',
      year: '2001'
    }
  ]);

  const [loading] = useState(false);

  if (loading) {
    return (
      <div className="about-loading">
        <div className="loading-spinner"></div>
        <p>Loading Academic Profile...</p>
      </div>
    );
  }

  return (
    <div className="about">
      {/* Hero Section */}
      <section className="about-hero">
        <div className="section-container">
          <div className="about-content">
            <motion.div
              initial={{ opacity: 0, x: -30 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.8 }}
              className="about-image"
            >
              <div className="profile-image-container">
                <img 
                  src={profileImage} 
                  alt={profile.name}
                  className="profile-image loaded"
                />
              </div>
            </motion.div>
            <motion.div
              initial={{ opacity: 0, x: 30 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.8, delay: 0.2 }}
              className="about-text"
            >
              <h1>{profile.name}</h1>
              <h2>{profile.title}</h2>
              
              <div className="contact-info-mini">
                <div className="contact-item">
                  <FaEnvelope className="contact-icon" />
                  <a href={`mailto:${profile.email}`} style={{ color: 'inherit', textDecoration: 'none' }}>{profile.email}</a>
                </div>

                <div className="contact-item">
                  <FaPhone className="contact-icon" />
                  <a href={`tel:${profile.phone}`} style={{ color: 'inherit', textDecoration: 'none' }}>{profile.phone}</a>
                </div>

                <div className="contact-item">
                  <FaMapMarkerAlt className="contact-icon" />
                  <span>{profile.address}</span>
                </div>
              </div>
              <p className="department">{profile.department}</p>
              <p className="institution">{profile.institution}</p>

              <div className="social-links">
                <a 
                  href="https://www.linkedin.com/in/vivek-shrivastava-4a838a2/" 
                  target="_blank" 
                  rel="noopener noreferrer" 
                  className="social-link"
                >
                  <FaLinkedin /> LinkedIn
                </a>
                <a 
                  href="https://scholar.google.com/citations?user=xR0COBoAAAAJ&hl=en" 
                  target="_blank" 
                  rel="noopener noreferrer" 
                  className="social-link"
                >
                  <FaGoogle /> Google Scholar
                </a>
                <a 
                  href="https://portfolios.nituk.ac.in/453/dr-vivek-shrivastava/personal-details" 
                  target="_blank" 
                  rel="noopener noreferrer" 
                  className="social-link"
                >
                  <FaUniversity /> NIT UK Profile
                </a>
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Bio Section */}
      <section className="about-bio">
        <div className="section-container">
          <div className="section-header">
            <h2 className="section-title">Biosketch</h2>
            <p className="section-subtitle">
              Distinguished academic, researcher, and administrator with over two decades of global experience.
            </p>
          </div>
          <div className="bio-content">
            <p>{profile.bio}</p>
          </div>
        </div>
      </section>

      {/* Career Highlights */}
      <section className="career-highlights">
        <div className="section-container">
          <div className="section-header">
            <h2 className="section-title">Academic & Professional Positions</h2>
          </div>
          <div className="highlights-grid">
            {careerPositions.map((pos, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.1 }}
                className="highlight-card"
              >
                <FaUserTie className="highlight-icon" />
                <h3>{pos.role}</h3>
                <p>{pos.organization}</p>
                <span className="highlight-year">{pos.period}</span>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Research Interests */}
      {profile.researchInterests && profile.researchInterests.length > 0 && (
        <section className="research-interests">
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
                  transition={{ delay: index * 0.1 }}
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
      )}

      {/* Education Section */}
      {education.length > 0 && (
        <section className="education-section">
          <div className="section-container">
            <div className="section-header">
              <h2 className="section-title">
                <FaGraduationCap /> Education & Qualifications
              </h2>
              <p className="section-subtitle">Educational background and academic achievements</p>
            </div>
            <div className="education-timeline">
              {education.map((edu, index) => (
                <motion.div
                  key={edu._id || index}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.1 }}
                  className="education-item"
                >
                  <div className="education-year">{edu.year}</div>
                  <div className="education-content">
                    <h3>{edu.degree}</h3>
                    <p className="education-institution">{edu.institution}</p>
                    {edu.field && <p className="education-field">{edu.field}</p>}
                  </div>
                </motion.div>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* Administrative Roles */}
      {profile.administrativeRoles && profile.administrativeRoles.length > 0 && (
        <section className="administrative-roles">
          <div className="section-container">
            <div className="section-header">
              <h2 className="section-title">Administrative Roles & Services</h2>
              <p className="section-subtitle">Professional service and academic leadership contributions</p>
            </div>
            <div className="roles-list">
              {profile.administrativeRoles.map((role, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: index * 0.05 }}
                  className="role-item"
                >
                  <div className="role-bullet">•</div>
                  <p>{role}</p>
                </motion.div>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* Professional Memberships */}
      {profile.professionalMemberships && profile.professionalMemberships.length > 0 && (
        <section className="professional-memberships">
          <div className="section-container">
            <div className="section-header">
              <h2 className="section-title">Professional Memberships</h2>
              <p className="section-subtitle">Academic and professional affiliations</p>
            </div>
            <div className="memberships-grid">
              {profile.professionalMemberships.map((membership, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, scale: 0.9 }}
                  animate={{ opacity: 1, scale: 1 }}
                  transition={{ delay: index * 0.1 }}
                  className="membership-card"
                >
                  <FaGraduationCap className="membership-icon" />
                  <p>{membership}</p>
                </motion.div>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* Honors & Awards */}
      {profile.awards && profile.awards.length > 0 && (
        <section className="honors-awards">
          <div className="section-container">
            <div className="section-header">
              <h2 className="section-title">Research Highlights & Achievements</h2>
              <p className="section-subtitle">Academic recognition, funding, and excellence</p>
            </div>
            <div className="awards-list">
              {profile.awards.map((award, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, x: 20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: index * 0.05 }}
                  className="award-item"
                >
                  <div className="award-bullet">★</div>
                  <p>{award}</p>
                </motion.div>
              ))}
            </div>
          </div>
        </section>
      )}
    </div>
  );
};

export default About;