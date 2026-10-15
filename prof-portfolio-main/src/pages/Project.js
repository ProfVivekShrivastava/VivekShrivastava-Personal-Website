import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { FaUserTie, FaCalendarAlt, FaUniversity, FaChalkboardTeacher, FaGlobe } from 'react-icons/fa';
import './Project.css';

const Projects = () => {
  const [activeTab, setActiveTab] = useState('admin');

  const administrativeRoles = [
    {
      institution: 'NIT Uttarakhand',
      period: 'Jan 2024 - Till date',
      role: 'Dean (International Relations, Alumni Affairs & Ranking)'
    },
    {
      institution: 'NIT Delhi',
      period: 'Mar ‘18 - Jan 24',
      role: 'Nodal Officer (Ek Bharat Shreshtha Bharat)'
    },
    {
      institution: 'NIT Delhi',
      period: 'Mar ‘18 - Jan 24',
      role: 'Nodal Officer- AICTE (Deemed University Exam)'
    },
    {
      institution: 'NIT Delhi',
      period: 'Aug 2022 - Jan 2023',
      role: 'Head of the Department'
    },
    {
      institution: 'NIT Delhi',
      period: '2022',
      role: 'Faculty In-charge, DASA-2022 (Foreign Admission 2022)'
    },
    {
      institution: 'NIT Delhi',
      period: 'Oct 2021 - Aug 2022 & Aug 2018 - Jul 2021',
      role: 'Dean (Research & Consultancy)'
    },
    {
      institution: 'NIT Delhi',
      period: 'June 2021 - June 2022',
      role: 'Registrar (I/c)'
    },
    {
      institution: 'NIT Delhi',
      period: '2021',
      role: 'Faculty In-charge, CCMT-2021 (PG Admission 2021)'
    },
    {
      institution: 'NIT Delhi',
      period: '2021',
      role: 'Faculty In-charge, CSAB-2021 (UG Admission 2021)'
    },
    {
      institution: 'NIT Delhi',
      period: 'May 2021 - Oct 2021',
      role: 'Dean (Faculty Welfare)'
    },
    {
      institution: 'NIT Delhi',
      period: '2020',
      role: 'Faculty In-charge, CSAB-2020 (UG Admission 2020)'
    },
    {
      institution: 'NIT Delhi',
      period: '2019',
      role: 'Faculty In-charge, CSAB-2019 (UG Admission 2019)'
    },
    {
      institution: 'NIT Delhi',
      period: 'Mar 2018 - Dec 2019',
      role: 'Dean (Student Welfare)'
    },
    {
      institution: 'NIT Delhi',
      period: 'Aug 2018 - Oct 2021',
      role: 'Chairman, Anti-ragging committee'
    },
    {
      institution: 'NIT Delhi',
      period: 'Sep 2018 - Apr 2020',
      role: 'Chairman, Committee for policy/guidelines framing'
    },
    {
      institution: 'NIT Delhi',
      period: "Jun '18 - Oct '18",
      role: 'Director (I/c)'
    },
    {
      institution: 'NIT Delhi',
      period: 'Mar 2018 - Oct 2021',
      role: 'Chairman Start up India'
    },
    {
      institution: 'RTU Kota',
      period: '2017',
      role: 'Convener, CAM-2017'
    },
    {
      institution: 'RTU Kota',
      period: 'May’ 15 - Mar ‘18',
      role: 'Associate Dean (Research)'
    },
    {
      institution: 'RTU Kota',
      period: 'May’ 15 - Mar ‘18',
      role: 'Co-coordinator, CAM 2015'
    },
    {
      institution: 'RTU Kota',
      period: 'July’15 - June’ 16',
      role: 'Member, Departmental Central Academic Monitoring Cells'
    },
    {
      institution: 'RTU Kota',
      period: 'July’15 - June’ 16',
      role: 'Member, Departmental Exam Committee'
    },
    {
      institution: 'RTU Kota',
      period: 'April’ 15 - Mar ‘18',
      role: 'Coordinator, Incubator Centre'
    },
    {
      institution: 'RTU Kota',
      period: 'May’ 14 - Mar ‘18',
      role: 'Member Secretary, Departmental Accreditation Committee'
    },
    {
      institution: 'RTU Kota',
      period: 'May’ 14 - Mar ‘18',
      role: 'In charge Power System, TEQIP Departmental Committee'
    },
    {
      institution: 'RTU Kota',
      period: 'Jan’ 14 - Mar ‘18',
      role: 'Member Secretary, Departmental NBA work'
    },
    {
      institution: 'RTU Kota',
      period: 'Jun’ 14 - Sep’ 14',
      role: 'In charge, Faculty Recruitment'
    },
    {
      institution: 'RTU Kota',
      period: 'July’ 14 - Mar ‘18',
      role: 'Member, Result Declaration Committee'
    },
    {
      institution: 'RTU Kota',
      period: 'Oct’ 14 - Mar ‘18',
      role: 'Coordinator Tech Fest 2015'
    },
    {
      institution: 'RTU Kota',
      period: 'July’14 - June’ 15',
      role: 'Member, Departmental Central Academic Monitoring Cells'
    },
    {
      institution: 'RTU Kota',
      period: 'July’14 - June’ 15',
      role: 'Member, Departmental Exam Committee'
    },
    {
      institution: 'RTU Kota',
      period: 'June’ 14 - Mar ‘18',
      role: 'Member, Board of Studies (Electrical Engineering)'
    },
    {
      institution: 'RTU Kota',
      period: 'June’ 14 - Oct’ 14',
      role: 'Co-coordinator, RTU DAT-2014'
    },
    {
      institution: 'RTU Kota',
      period: 'Oct.’ 14 - May’15',
      role: 'Faculty In-charge Training & Placement Cell'
    },
    {
      institution: 'RTU Kota',
      period: 'Dec’ 14 - Mar ‘18',
      role: 'Member Secretary, Members of Academic Council'
    },
    {
      institution: 'RTU Kota',
      period: 'Academic Session 2013-14',
      role: 'Member, Evaluation Review Committee'
    },
    {
      institution: 'RTU Kota',
      period: 'Academic Session 2013-14',
      role: 'Member, Feedback Review Committees'
    },
    {
      institution: 'NIT Delhi & RTU Kota',
      period: 'April’ 13 - Till date',
      role: 'Observer CBSE/UGC Examinations'
    },
    {
      institution: 'NIT Delhi',
      period: '25 Aug 2012 - 30 Aug 2013',
      role: 'Academic In-charge'
    },
    {
      institution: 'NIT Delhi',
      period: '25 Aug 2012 - 30 Aug 2013',
      role: 'Examination In-charge'
    },
    {
      institution: 'NIT Delhi',
      period: '01 Sep 2012 - 30 Aug 2013',
      role: 'Chairman Library Committee'
    },
    {
      institution: 'NIT Delhi',
      period: '01 Sep 2012 - 30 Aug 2013',
      role: 'Deputy Centre In charge (B. Tech) Counseling'
    },
    {
      institution: 'NIT Delhi',
      period: '01 Sep 2012 - 30 Aug 2013',
      role: 'Coordinator, Guest Faculty'
    },
    {
      institution: 'NIT Delhi',
      period: '01 Sep 2012 - 30 Aug 2013',
      role: 'Member, Hostel Management Committee'
    },
    {
      institution: 'NIT Delhi',
      period: '01 Sep 2012 - 30 Aug 2013',
      role: 'Warden'
    },
    {
      institution: 'NIT Delhi',
      period: '01 Sep 2012 - 30 Aug 2013',
      role: 'Chairman Anti-Ragging Committee'
    },
    {
      institution: 'NIT Delhi',
      period: '25 Aug 2012 - 30 Aug 2013',
      role: 'Coordinator B. Tech. Programme (EEE)'
    }
  ];

  const facultyPrograms = [
    {
      title: 'Reliability Studies For Engineering Applications',
      period: '13 Feb 2023 – 24 Feb 2023 (02 Weeks)',
      organizer: 'AICTE (ATAL) Academy'
    },
    {
      title: 'Design Test and validate Power Electronics E-mobility Renewable Microgrid using Typhoon HIL',
      period: '27 Jun 2022 - 2 July 2022',
      organizer: 'Typhoon HIL Quarbz Info'
    },
    {
      title: 'Wind Power Based Distributed Generation',
      period: '29 Apr 2022 – 04 May 2022',
      organizer: 'GIAN IIT Kharagpur'
    },
    {
      title: 'Nature Inspired Optimization Techniques',
      period: '19 July 2021 - 23 July 2021',
      organizer: 'AICTE (ATAL) Academy'
    },
    {
      title: 'Emerging Trends in Electromechanical System & Renewable Energy',
      period: '10 March 2021 - 14 March 2021',
      organizer: 'Self Sponsored'
    },
    {
      title: 'Power Electronics Interfaces for Green Energy Systems',
      period: '01 Feb 2021 - 05 Feb 2021',
      organizer: 'Self Sponsored'
    },
    {
      title: 'Integration of Alternate Energy Resources in Smart Grid',
      period: '25 Dec 2020 - 29 Dec 2020',
      organizer: 'AICTE (ATAL) Academy'
    },
    {
      title: 'Power System Reliability',
      period: '26 Oct 2020 - 30 Oct 2020',
      organizer: 'AICTE (ATAL) Academy'
    },
    {
      title: 'Transition in Power Electronics towards Sustainable, Smart and Flexible Micro-Grids',
      period: '19 Oct 2020 - 23 Oct 2020',
      organizer: 'National Mission on Power Electronics Technology Phase III'
    },
    {
      title: 'Advance Trends in Reliability Solution for Engineering Applications',
      period: '17 Dec 2016 - 21 Dec 2016',
      organizer: 'TEQIP-II'
    },
    {
      title: 'Optimization Techniques Using Nature Inspired Algorithms for Engineering Applications',
      period: '19 Jan 2015 - 23 Jan 2015',
      organizer: 'TEQIP-II'
    }
  ];

  const conferences = [
    {
      name: '2nd International Conference on Power Engineering and Intelligent Systems (PEIS2024)',
      period: 'Mar 16-17, 2024',
      organizer: 'Soft Computing Research Society'
    },
    {
      name: '5th International Conference on Communication and Intelligent Systems (ICCIS 2023)',
      period: 'Dec 16-17, 2023',
      organizer: 'Soft Computing Research Society'
    },
    {
      name: 'International Conference on Power Engineering and Intelligent Systems (PEIS2023)',
      period: 'Jun 24-25, 2023',
      organizer: 'Soft Computing Research Society'
    },
    {
      name: '2nd International Conference of Undergraduate Students (ICUS 2023)',
      period: 'May 20-21, 2023',
      organizer: 'Soft Computing Research Society'
    },
    {
      name: '4th International Conference on Communication and Intelligent Systems (ICCIS 2022)',
      period: 'Dec 19-20, 2022',
      organizer: 'Soft Computing Research Society'
    },
    {
      name: 'IEEE 10th Power India International Conference 2022 (PIICON 2022)',
      period: '25th - 27th Nov 2022',
      organizer: 'IEEE USA'
    },
    {
      name: 'Congress on Research in Engineering, Science and Management (CRESM 2022)',
      period: 'March 10-12, 2022',
      organizer: 'Soft Computing Research Society'
    },
    {
      name: '3rd International Conference on Communication and Intelligent Systems (ICCIS 2021)',
      period: 'Dec 18-19, 2021',
      organizer: 'Soft Computing Research Society'
    },
    {
      name: 'International Conference of Undergraduate Students (ICUS 2022)',
      period: 'Nov 27-28, 2021',
      organizer: 'Soft Computing Research Society'
    },
    {
      name: 'International Conference on Energy, Material Science and Mechanical Engineering (EMSME-2020)',
      period: '30 Oct - 1 Nov, 2020',
      organizer: 'Typhoon HIL Quarbz Info'
    }
  ];

  return (
    <div className="projects-page">
      <section className="projects-hero">
        <div className="section-container">
          <div className="section-header">
            <h1 className="section-title">Leadership, Programs & Conferences</h1>
            <p className="section-subtitle">
              Comprehensive overview of administrative responsibilities, faculty development programs, and scholarly conferences.
            </p>
          </div>

          {/* Navigation Tabs */}
          <div className="projects-tabs">
            <button 
              className={`tab-btn ${activeTab === 'admin' ? 'active' : ''}`}
              onClick={() => setActiveTab('admin')}
            >
              <FaUserTie /> Administrative & Leadership Roles
            </button>
            <button 
              className={`tab-btn ${activeTab === 'programs' ? 'active' : ''}`}
              onClick={() => setActiveTab('programs')}
            >
              <FaChalkboardTeacher /> Faculty Development Programs
            </button>
            <button 
              className={`tab-btn ${activeTab === 'conferences' ? 'active' : ''}`}
              onClick={() => setActiveTab('conferences')}
            >
              <FaGlobe /> Conferences & Events
            </button>
          </div>
        </div>
      </section>

      {/* Tab Content Section */}
      <section className="projects-content-section">
        <div className="section-container">
          
          {/* Administrative Roles Tab */}
          {activeTab === 'admin' && (
            <div className="projects-grid">
              {administrativeRoles.map((item, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.03 }}
                  className="project-card"
                >
                  <div className="card-top">
                    <FaUniversity className="card-icon" />
                    <span className="card-institution">{item.institution}</span>
                  </div>
                  <h3>{item.role}</h3>
                  <div className="card-footer">
                    <FaCalendarAlt />
                    <span>{item.period}</span>
                  </div>
                </motion.div>
              ))}
            </div>
          )}

          {/* Faculty Development Programs Tab */}
          {activeTab === 'programs' && (
            <div className="projects-grid">
              {facultyPrograms.map((item, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.05 }}
                  className="project-card"
                >
                  <div className="card-top">
                    <FaChalkboardTeacher className="card-icon" />
                    <span className="card-institution">{item.organizer}</span>
                  </div>
                  <h3>{item.title}</h3>
                  <div className="card-footer">
                    <FaCalendarAlt />
                    <span>{item.period}</span>
                  </div>
                </motion.div>
              ))}
            </div>
          )}

          {/* Conferences Tab */}
          {activeTab === 'conferences' && (
            <div className="projects-grid">
              {conferences.map((item, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.05 }}
                  className="project-card"
                >
                  <div className="card-top">
                    <FaGlobe className="card-icon" />
                    <span className="card-institution">{item.organizer}</span>
                  </div>
                  <h3>{item.name}</h3>
                  <div className="card-footer">
                    <FaCalendarAlt />
                    <span>{item.period}</span>
                  </div>
                </motion.div>
              ))}
            </div>
          )}

        </div>
      </section>
    </div>
  );
};

export default Projects;