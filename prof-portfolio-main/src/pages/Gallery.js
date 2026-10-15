import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { FaSearchPlus, FaTimes, FaChevronLeft, FaChevronRight, FaImages } from 'react-icons/fa';
import './Gallery.css';

// Import images from assets sub-directory (src/assets/gallery/)
import img1 from '../assets/gallery/1.jpg';
import img2 from '../assets/gallery/2.jpg';
import img3 from '../assets/gallery/3.jpg';
import img4 from '../assets/gallery/4.jpg';
import img5 from '../assets/gallery/5.jpg';
import img6 from '../assets/gallery/6.jpg';
import img7 from '../assets/gallery/7.jpg';
import img8 from '../assets/gallery/8.jpg';
import img9 from '../assets/gallery/9.jpg';
import img10 from '../assets/gallery/10.jpg';
import img11 from '../assets/gallery/11.jpg';
import img12 from '../assets/gallery/12.png';
import img13 from '../assets/gallery/13.jpg';
import img14 from '../assets/gallery/14.jpg';

const galleryData = [
  { id: 1, src: img1, caption: '' },
  { id: 2, src: img2, caption: '' },
  { id: 3, src: img3, caption: '' },
  { id: 4, src: img4, caption: '' },
  { id: 5, src: img5, caption: '' },
  { id: 6, src: img6, caption: '' },
  { id: 7, src: img7, caption: '' },
  { id: 8, src: img8, caption: '' },
  { id: 9, src: img9, caption: '' },
  { id: 10, src: img10, caption: '' },
  { id: 11, src: img11, caption: '' },
  { id: 12, src: img12, caption: '' },
  { id: 13, src: img13, caption: '' },
  { id: 14, src: img14, caption: '' },
];

/* Category options (commented out as requested)
const categories = ['All', 'Conferences', 'Campus', 'Workshops', 'Academic'];
*/

const Gallery = () => {
  // Category state (commented out)
  // const [selectedCategory, setSelectedCategory] = useState('All');
  
  const [activeImageIndex, setActiveImageIndex] = useState(null);

  // Filtered items (using galleryData directly without category filtering)
  const items = galleryData;

  // Keyboard navigation for lightbox
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (activeImageIndex === null) return;
      if (e.key === 'Escape') setActiveImageIndex(null);
      if (e.key === 'ArrowRight') handleNext();
      if (e.key === 'ArrowLeft') handlePrev();
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  });

  const handlePrev = () => {
    if (activeImageIndex === null) return;
    setActiveImageIndex((prev) => (prev > 0 ? prev - 1 : items.length - 1));
  };

  const handleNext = () => {
    if (activeImageIndex === null) return;
    setActiveImageIndex((prev) => (prev < items.length - 1 ? prev + 1 : 0));
  };

  return (
    <div className="gallery-page">
      {/* Hero Section */}
      <section className="gallery-hero">
        <div className="section-container">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="gallery-hero-text"
          >
            <h1 className="page-title">Photo Gallery</h1>
            <p className="page-subtitle">
              Moments, academic conferences, faculty programs, and institutional leadership events
            </p>
          </motion.div>
        </div>
      </section>

      {/* Gallery Content Section */}
      <section className="gallery-content">
        <div className="section-container">
          {/* Category Filter Tabs (Commented out)
          <div className="gallery-filters">
            {categories.map((cat) => (
              <button
                key={cat}
                className={`filter-btn ${selectedCategory === cat ? 'active' : ''}`}
                onClick={() => setSelectedCategory(cat)}
              >
                {cat}
              </button>
            ))}
          </div>
          */}

          {/* Photos Grid */}
          {items.length === 0 ? (
            <div className="no-photos">
              <FaImages size={60} />
              <h3>No photos found</h3>
            </div>
          ) : (
            <motion.div layout className="gallery-grid">
              <AnimatePresence>
                {items.map((item, index) => (
                  <motion.div
                    key={item.id}
                    layout
                    initial={{ opacity: 0, scale: 0.9 }}
                    animate={{ opacity: 1, scale: 1 }}
                    exit={{ opacity: 0, scale: 0.9 }}
                    transition={{ duration: 0.4 }}
                    className="gallery-card"
                    onClick={() => setActiveImageIndex(index)}
                  >
                    <div className="gallery-image-wrapper">
                      <img src={item.src} alt={item.title || item.caption || `Gallery photo ${item.id}`} loading="lazy" />
                      <div className="gallery-overlay">
                        <div className="overlay-icon">
                          <FaSearchPlus />
                        </div>
                      </div>
                    </div>
                    {(item.title || item.caption) && (
                      <div className="gallery-card-info">
                        {item.title && <h3 className="card-title">{item.title}</h3>}
                        {item.caption && <p className="card-caption">{item.caption}</p>}
                      </div>
                    )}
                  </motion.div>
                ))}
              </AnimatePresence>
            </motion.div>
          )}
        </div>
      </section>

      {/* Lightbox Modal */}
      <AnimatePresence>
        {activeImageIndex !== null && items[activeImageIndex] && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="lightbox-backdrop"
            onClick={() => setActiveImageIndex(null)}
          >
            <div className="lightbox-modal" onClick={(e) => e.stopPropagation()}>
              <button
                className="lightbox-close"
                onClick={() => setActiveImageIndex(null)}
                aria-label="Close modal"
              >
                <FaTimes />
              </button>

              {items.length > 1 && (
                <>
                  <button
                    className="lightbox-nav prev"
                    onClick={handlePrev}
                    aria-label="Previous image"
                  >
                    <FaChevronLeft />
                  </button>
                  <button
                    className="lightbox-nav next"
                    onClick={handleNext}
                    aria-label="Next image"
                  >
                    <FaChevronRight />
                  </button>
                </>
              )}

              <div className="lightbox-image-container">
                <img
                  src={items[activeImageIndex].src}
                  alt={items[activeImageIndex].title || items[activeImageIndex].caption || 'Full view'}
                />
              </div>

              <div className="lightbox-details">
                {items[activeImageIndex].title && (
                  <h3 className="lightbox-title">{items[activeImageIndex].title}</h3>
                )}
                {items[activeImageIndex].caption && (
                  <p className="lightbox-caption">{items[activeImageIndex].caption}</p>
                )}
                <span className="lightbox-counter">
                  {activeImageIndex + 1} / {items.length}
                </span>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

export default Gallery;
