import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { FaChalkboardTeacher, FaBook, FaGraduationCap, FaCalendar, FaUsers, FaMicrophone, FaLaptop, FaGlobe } from 'react-icons/fa';
import './Teaching.css';

const Teaching = () => {
  const [courses] = useState([
    {
      _id: '1',
      courseName: 'Introduction to Electrical and Electronics Engineering',
      courseCode: 'ECE/EEE Core',
      level: 'Undergraduate',
      semester: 'As per University Schedule',
      program: 'B.Tech.',
      description:
        'Fundamental concepts of electrical circuits, electronic components, basic signal analysis, and engineering applications for first-year engineering students.',
      focus: 'Basic electrical circuits, electronics fundamentals, engineering applications'
    },
    {
      _id: '2',
      courseName: 'Electronics Engineering Workshop',
      courseCode: 'ECE Lab',
      level: 'Undergraduate',
      semester: 'As per University Schedule',
      program: 'B.Tech.',
      description:
        'Hands-on laboratory course focusing on electronic components, circuit assembly, measurements, and practical understanding of electronic systems.',
      focus: 'Practical electronics, measurements, circuit implementation'
    },
    {
      _id: '3',
      courseName: 'Mathematics for Engineers',
      courseCode: 'Engineering Mathematics',
      level: 'Undergraduate',
      semester: 'As per University Schedule',
      program: 'B.Tech.',
      description:
        'Mathematical foundations for engineering including calculus, linear algebra, and differential equations relevant to electronics and communication systems.',
      focus: 'Engineering mathematics, problem solving, analytical techniques'
    }
  ]);

  const [conferences] = useState([
    {
      _id: '1',
      title: 'National Seminar on MEMS & Nano Technology',
      type: 'Seminar',
      venue: 'Trident Academy of Technology, Bhubaneswar',
      level: 'National',
      date: '04-05 October, 2012',
      sponsoringAgency: 'Trident Academy of Technology'
    },
    {
      _id: '2',
      title: 'Speech Signal Processing and its Applications',
      type: 'Seminar',
      venue: 'BCET, Balasore',
      level: 'National',
      date: '20-21 September, 2013',
      sponsoringAgency: 'AICTE'
    },
    {
      _id: '3',
      title: 'Introduction to Matlab & its applications',
      type: 'Faculty Development Programme',
      venue: 'Trident Academy of Technology, Bhubaneswar',
      level: 'National',
      date: '19-31 December, 2011',
      sponsoringAgency: ''
    },
    {
      _id: '4',
      title: 'Recent trends in Medical Imaging using VLSI',
      type: 'Staff Development Programme',
      venue: 'Orissa Engineering College, Bhubaneswar',
      level: 'National',
      date: '16-18 March, 2012',
      sponsoringAgency: 'AICTE'
    },
    {
      _id: '5',
      title: 'Active and Passive Device Characterization using Anritsu VNA',
      type: 'Workshop',
      venue: 'Department of Electronics Engineering, IIT (BHU), Varanasi',
      level: 'National',
      date: '14 October, 2017',
      sponsoringAgency: 'IEEE'
    },
    {
      _id: '6',
      title: 'Avenues in Aeronautical R&D for Indian Defence',
      type: 'Seminar',
      venue: 'Department of Electronics Engineering, IIT (BHU), Varanasi',
      level: 'National',
      date: '10 March, 2018',
      sponsoringAgency: ''
    },
    {
      _id: '7',
      title: 'Recent Advances on Passive and Active Components at High Frequencies',
      type: 'Training Programme',
      venue: 'Department of Electronics Engineering, IIT (BHU), Varanasi',
      level: 'National',
      date: '25-30 June, 2018',
      sponsoringAgency: 'QIP'
    },
    {
      _id: '8',
      title: 'LaTex for Beginners',
      type: 'Workshop',
      venue: 'Department of Electrical Engineering, IIT (BHU), Varanasi',
      level: 'National',
      date: '06 October, 2018',
      sponsoringAgency: 'IEEE'
    },
    {
      _id: '9',
      title: 'Recent Trends in Microwave/Millimeter Wave Technology and their Applications in Wireless Communication and Defense Perspective',
      type: 'Training Programme',
      venue: 'Department of Electronics Engineering, IIT (BHU) Varanasi',
      level: 'National',
      date: '14-19 October, 2019',
      sponsoringAgency: 'QIP'
    },
    {
      _id: '10',
      title: 'Metamaterials and its applications',
      type: 'Workshop',
      venue: 'Malaviya National Institute of Technology, Jaipur / Government Women Engineering College',
      level: 'International',
      date: '27-31 July, 2020',
      sponsoringAgency: 'IEEE Antennas and Propagation Society'
    },
    {
      _id: '11',
      title: 'Advanced Antennas for Space and Industrial Applications: Design, Modelling, hardware and Test',
      type: 'Workshop',
      venue: 'IEEE MTT-S Kerala Chapter / IIST / GECBH, Thiruvananthapuram',
      level: 'National',
      date: '02-03 December, 2020',
      sponsoringAgency: 'IEEE MTT-S / IEEE APS'
    },
    {
      _id: '12',
      title: 'Microwave and Antenna Applications in 5G',
      type: 'Workshop',
      venue: 'IEEE Bangalore Section',
      level: 'National',
      date: '08-13 December, 2020',
      sponsoringAgency: 'IEEE'
    },
    {
      _id: '13',
      title: 'Different Computational Electromagnetic Techniques and Their Applications',
      type: 'Workshop',
      venue: 'Jadavpur University',
      level: 'National',
      date: '27-29 December, 2020',
      sponsoringAgency: 'IEEE MTT-S Student Branch Chapter'
    },
    {
      _id: '14',
      title: 'Data Analytics and Predictive Technology Driven IOT Based Smart Grid Infrastructure',
      type: 'Short-Term Course',
      venue: 'IIT (BHU) Varanasi',
      level: 'National',
      date: '01-06 March, 2021',
      sponsoringAgency: 'DST / I-DAPT HUB Foundation'
    },
    {
      _id: '15',
      title: 'Modern Antennas for present and Futuristic Wireless Communication Technology',
      type: 'Workshop',
      venue: 'NIT Sikkim',
      level: 'National',
      date: '08-13 March, 2021',
      sponsoringAgency: 'TEQIP-III'
    },
    {
      _id: '16',
      title: 'IEEE UP Section (India) Student Chair Meet',
      type: 'Meetup',
      venue: 'Virtual',
      level: 'National',
      date: '06 June, 2021',
      sponsoringAgency: 'IEEE UP Section'
    }
  ]);


  const levelColors = {
    'Undergraduate': '#0066cc',
    'Postgraduate': '#28a745',
    'Doctoral': '#dc3545',
    'International': '#9c27b0',
    'National': '#ff9800',
    'University': '#607d8b',
    'State': '#795548'
  };

  const typeIcons = {
    'Conference': FaMicrophone,
    'Workshop': FaLaptop,
    'Seminar': FaUsers,
    'Webinar': FaGlobe,
    'Training Programme': FaGraduationCap,
    'Symposium': FaMicrophone,
    'In-Service Training': FaChalkboardTeacher,
    'Faculty Development Programme': FaUsers,
    'Short-Term Course': FaBook,
    'Meetup': FaUsers,
    'Refresher Course': FaBook,
    'Staff Development Programme': FaUsers
  };

  const [activeTab, setActiveTab] = useState('courses');

  return (
    <div className="teaching">
      <section className="teaching-hero">
        <div className="section-container">
          <div className="hero-text">
            <h1 className="page-title">Teaching</h1>
            <p className="page-subtitle">
              Academic instruction, research, and professional engagements in Electrical and Electronics Engineering at National Institute of Technology (NIT) Uttarakhand
            </p>
          </div>
        </div>
      </section>

<section className="teaching-content">
  <div className="section-container">
    <div className="teaching-overview">
      <h2>Areas of Specialization</h2>
      <div className="specialization-tags">
        <span className="specialization-tag">Smart Metasurface</span>
        <span className="specialization-tag">Planar Antenna</span>
        <span className="specialization-tag">Electromagnetics</span>
        <span className="specialization-tag">5G (sub-6 GHz and mm-Wave), 6G and Beyond Applications</span>
        <span className="specialization-tag">Reconfigurable Antennas</span>
        <span className="specialization-tag">Wearable/Implantable Antennas for Biomedical and IoT Applications</span>
      </div>
    </div>


          <div className="teaching-tabs">
            <button 
              className={activeTab === 'courses' ? 'active' : ''}
              onClick={() => setActiveTab('courses')}
            >
              <FaBook /> Courses Taught
            </button>
            <button 
              className={activeTab === 'conferences' ? 'active' : ''}
              onClick={() => setActiveTab('conferences')}
            >
              <FaMicrophone /> Conferences & Workshops ({conferences.length})
            </button>
          </div>

          {activeTab === 'courses' && (
            <div className="courses-section">
              <h2>Courses Currently Teaching</h2>
              {courses.length === 0 ? (
                <div className="no-courses">
                  <FaBook size={60} />
                  <p>No courses available. Check back later!</p>
                </div>
              ) : (
                <div className="courses-grid">
                  {courses.map((course, index) => (
                    <motion.div
                      key={course._id || index}
                      initial={{ opacity: 0, y: 20 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ delay: index * 0.1 }}
                      className="course-card"
                    >
                      <div className="course-header">
                        <div 
                          className="course-level"
                          style={{ backgroundColor: levelColors[course.level] || '#6c757d' }}
                        >
                          {course.level}
                        </div>
                        <div className="course-program">{course.program}</div>
                      </div>

                      <h3 className="course-name">{course.courseName}</h3>
                      <p className="course-code">{course.courseCode}</p>

                      <div className="course-details">
                        <div className="detail-item">
                          <FaGraduationCap />
                          <span>{course.program} Program</span>
                        </div>
                        <div className="detail-item">
                          <FaCalendar />
                          <span>{course.semester}</span>
                        </div>
                      </div>

                      <p className="course-description">{course.description}</p>

                      {course.focus && (
                        <div className="course-focus">
                          <strong>Focus Areas:</strong> {course.focus}
                        </div>
                      )}
                    </motion.div>
                  ))}
                </div>
              )}
            </div>
          )}

          {activeTab === 'conferences' && (
            <div className="conferences-section">
              <h2>Conference Presentations & Workshops</h2>
              {conferences.length === 0 ? (
                <div className="no-conferences">
                  <FaMicrophone size={60} />
                  <p>No conference data available.</p>
                </div>
              ) : (
                <div className="conferences-list">
                  {conferences.map((conf, index) => {
                    const TypeIcon = typeIcons[conf.type] || FaMicrophone;
                    return (
                      <motion.div
                        key={conf._id || index}
                        initial={{ opacity: 0, x: -20 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: index * 0.05 }}
                        className="conference-card"
                      >
                        <div className="conference-header">
                          <div 
                            className="conference-level"
                            style={{ backgroundColor: levelColors[conf.level] || '#6c757d' }}
                          >
                            {conf.level}
                          </div>
                          <div className="conference-type">
                            <TypeIcon />
                            <span>{conf.type}</span>
                          </div>
                        </div>

                        <h3 className="conference-title">{conf.title}</h3>
                        
                        <div className="conference-details">
                          <div className="detail-item">
                            <FaCalendar />
                            <span>{conf.date}</span>
                          </div>
                          <div className="detail-item">
                            <FaGlobe />
                            <span>{conf.venue}</span>
                          </div>
                          {conf.sponsoringAgency && (
                            <div className="detail-item">
                              <FaUsers />
                              <span>Sponsored by: {conf.sponsoringAgency}</span>
                            </div>
                          )}
                        </div>
                      </motion.div>
                    );
                  })}
                </div>
              )}
            </div>
          )}
        </div>
      </section>
    </div>
  );
};

export default Teaching;