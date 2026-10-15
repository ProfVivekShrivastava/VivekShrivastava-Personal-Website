import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { FaFlask, FaCalendar, FaUsers, FaDollarSign } from 'react-icons/fa';
import './Research.css';

// Research data - using local data instead of backend API
const researchData = [
  {
    _id: '1',
    title: 'Smart Metasurface-Enabled Circular Polarization Facilitating Dynamic Beam Control Optimized Antenna Design in mm-Wave Systems',
    description: 'Approved research project focused on developing smart metasurface-based antenna systems with dynamic beam control capabilities for millimeter-wave communication applications, enabling efficient circular polarization control and beam steering.',
    status: 'Ongoing',
    year: '2025',
    funding: 'ANRF (Anusandhan National Research Foundation) - File No.: ANRF/ARG/2025/011847/ENS',
    duration: 'Approved Project',
    collaborators: ['National Institute of Technology (NIT) Uttarakhand'],
    keywords: ['Metasurfaces', 'Circular Polarization', 'Beam Control', 'Millimeter-Wave', '5G/6G Communication']
  },
  {
    _id: '2',
    title: 'Optimized Metasurface Antennas for Enhanced Wireless Communication at Millimeter-Wave Frequencies',
    description: 'Faculty Research Programme (FRP) funded project aimed at designing and optimizing metasurface-integrated antennas for enhanced performance at millimeter-wave frequencies, supporting next-generation wireless communication systems.',
    status: 'Ongoing',
    year: '2025',
    funding: 'Faculty Research Programme (FRP) Grant IoE, India - File No.: IoE/2025-26/12/FRP',
    duration: 'Approved Project',
    collaborators: ['National Institute of Technology (NIT) Uttarakhand'],
    keywords: ['Metasurface Antennas', 'Wireless Communication', 'Millimeter-Wave', 'Optimization', '5G/6G Systems']
  },
  {
    _id: '3',
    title: 'Study of High-Performance Metasurface Antenna in Microwave Frequencies',
    description: 'Ph.D. thesis research on the design and analysis of high-performance metasurface-based antennas operating at microwave frequencies, with focus on gain enhancement, bandwidth improvement, and multiband operation for modern RF and wireless systems.',
    status: 'Completed',
    year: '2022',
    funding: 'IIT (BHU) Doctoral Programme',
    duration: 'Ph.D. Research',
    collaborators: ['Indian Institute of Technology (BHU), Varanasi', 'Dr. Somak Bhattacharyya (Advisor)'],
    keywords: ['Metasurfaces', 'Microwave Antennas', 'Gain Enhancement', 'Multiband Design', 'RF Engineering']
  },
  {
    _id: '4',
    title: 'Planar Periodic Leaky Wave Antennas for Imaging Application',
    description: 'M.Tech thesis research on the development of planar periodic leaky wave antenna structures optimized for imaging applications, demonstrating advanced antenna design techniques for specialized RF systems.',
    status: 'Completed',
    year: '2015',
    funding: 'IIT Kharagpur Masters Programme',
    duration: 'M.Tech Research',
    collaborators: ['Indian Institute of Technology, Kharagpur', 'Dr. M K Mandal (Advisor)'],
    keywords: ['Leaky Wave Antennas', 'Planar Antennas', 'Imaging Applications', 'Antenna Design', 'RF Systems']
  }
];

const Research = () => {
  const [research] = useState(researchData);

  const statusColors = {
    'Completed': '#28a745',
    'Ongoing': '#255674',
    'Future': '#d97706'
  };

  return (
    <div className="research">
      <section className="research-hero">
        <div className="section-container">
          <h1 className="page-title">Research Projects</h1>
          <p className="page-subtitle">
  Research contributions in Antenna Design, Metasurfaces, RF & Microwave Engineering, and Electromagnetic Compatibility
</p>
        </div>
      </section>

      <section className="research-content">
        <div className="section-container">
          {research.length === 0 ? (
            <div className="no-research">
              <FaFlask size={60} />
              <p>No research projects found. Check back later!</p>
            </div>
          ) : (
            <div className="research-grid">
              {research.map((project, index) => (
                <motion.div
                  key={project._id || index}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.1 }}
                  className="research-card"
                >
                  <div className="research-header">
                    <div 
                      className="status-badge"
                      style={{ backgroundColor: statusColors[project.status] }}
                    >
                      {project.status} • {project.year}
                    </div>
                    <h3>{project.title}</h3>
                  </div>

                  <p className="research-description">{project.description}</p>

                  <div className="research-details">
                    {project.funding && (
                      <div className="detail-item">
                        <FaDollarSign /> <span>{project.funding}</span>
                      </div>
                    )}
                    {project.duration && (
                      <div className="detail-item">
                        <FaCalendar /> <span>{project.duration}</span>
                      </div>
                    )}
                    {project.collaborators && project.collaborators.length > 0 && (
                      <div className="detail-item">
                        <FaUsers /> <span>{project.collaborators.join(', ')}</span>
                      </div>
                    )}
                  </div>

                  {project.keywords && project.keywords.length > 0 && (
                    <div className="research-keywords">
                      {project.keywords.map((keyword, idx) => (
                        <span key={idx} className="keyword-tag">{keyword}</span>
                      ))}
                    </div>
                  )}
                </motion.div>
              ))}
            </div>
          )}
        </div>
      </section>
    </div>
  );
};

export default Research;