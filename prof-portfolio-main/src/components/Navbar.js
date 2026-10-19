import React, { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { FaBars, FaTimes } from 'react-icons/fa';
import './Navbar.css';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const [isMobile, setIsMobile] = useState(
    () => typeof window !== 'undefined' && window.matchMedia('(max-width: 600px)').matches
  );
  const location = useLocation();

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  useEffect(() => {
    const mediaQuery = window.matchMedia('(max-width: 600px)');
    const handleBreakpointChange = (event) => {
      setIsMobile(event.matches);
      if (!event.matches) setIsOpen(false);
    };
    mediaQuery.addEventListener('change', handleBreakpointChange);
    return () => mediaQuery.removeEventListener('change', handleBreakpointChange);
  }, []);

  const toggleMenu = () => setIsOpen(!isOpen);

  const handleToggleKeyDown = (event) => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      toggleMenu();
    }
  };

  const navLinks = [
    { path: '/', label: 'Home' },
    { path: '/about', label: 'About' },
    { path: '/projects', label: 'Leadership' },
    { path: '/publications', label: 'Publications' },
    { path: '/gallery', label: 'Gallery' }
  ];

  return (
    <nav className={`navbar ${scrolled ? 'scrolled' : ''}`}>
      <div className="navbar-container">
        <Link to="/" className="navbar-logo">
          <img
            src={`${process.env.PUBLIC_URL}/nituk-logo.png`}
            alt=""
            className="navbar-emblem"
          />
          <div className="logo-text-group">
            <span className="logo-text">Dr. Vivek Shrivastava</span>
            <span className="logo-subtext">NIT Uttarakhand</span>
          </div>
        </Link>
        
        <div className={`navbar-menu ${isOpen ? 'active' : ''}`}>
          {navLinks.map((link) => (
            <Link
              key={link.path}
              to={link.path}
              className={`navbar-link ${location.pathname === link.path ? 'active' : ''}`}
              onClick={() => setIsOpen(false)}
            >
              {link.label}
            </Link>
          ))}
        </div>

        <div
          className="navbar-toggle"
          onClick={toggleMenu}
          onKeyDown={isMobile ? handleToggleKeyDown : undefined}
          role={isMobile ? 'button' : undefined}
          aria-label={isMobile ? (isOpen ? 'Close menu' : 'Open menu') : undefined}
          aria-hidden={!isMobile}
          tabIndex={isMobile ? 0 : -1}
        >
          {isOpen ? <FaTimes /> : <FaBars />}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;