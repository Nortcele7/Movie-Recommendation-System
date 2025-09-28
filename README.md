# Movie Recommendation System 🎬

A content-based movie recommendation system built with Python that suggests movies similar to your preferences. The system uses machine learning techniques to analyze movie features and provide personalized recommendations through an interactive web interface.

## 🌟 Features

- **Interactive Web Interface**: Built with Streamlit for easy-to-use movie selection and recommendations
- **Content-Based Filtering**: Recommends movies based on similarity to selected movies
- **TMDB Dataset**: Uses The Movie Database (TMDb) dataset with 5,000+ movies
- **Real-time Recommendations**: Get instant movie suggestions with a single click
- **Cosine Similarity**: Advanced similarity calculation for accurate recommendations

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Movie-Recommendation-System
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv mynewenv
   
   # On Windows
   mynewenv\Scripts\activate
   
   # On macOS/Linux
   source mynewenv/bin/activate
   ```

3. **Install required packages**
   ```bash
   pip install streamlit pandas numpy scikit-learn
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501` to access the application

## 📁 Project Structure

```
Movie-Recommendation-System/
│
├── app.py                              # Main Streamlit application
├── movie_recommendation_system.ipynb   # Jupyter notebook with data analysis and model building
├── movies_dict.pkl                     # Processed movie data (pickle file)
├── movies.pkl                         # Movie dataset (pickle file)
├── similarity.pkl                     # Precomputed similarity matrix
├── tmdb_5000_movies.csv              # Original TMDb movies dataset
├── tmdb_5000_credits.csv             # Movie credits dataset
├── mynewenv/                         # Virtual environment
└── README.md                         # Project documentation
```

## 🎯 How It Works

### 1. Data Processing
The system processes the TMDb dataset containing:
- **Movie Information**: Titles, genres, overview, keywords, cast, crew
- **Movie Metadata**: Budget, revenue, release date, runtime, ratings
- **5,000+ Movies**: Comprehensive dataset for diverse recommendations

### 2. Feature Engineering
- Combines multiple features: genres, keywords, cast, crew, overview
- Creates feature vectors for each movie
- Preprocesses text data for better similarity calculations

### 3. Similarity Calculation
- Uses **Cosine Similarity** to measure movie similarity
- Precomputed similarity matrix for fast recommendations
- Considers multiple movie attributes for accurate suggestions

### 4. Recommendation Engine
- Finds the most similar movies to user selection
- Returns top 5 recommendations
- Real-time processing through Streamlit interface

## 🛠️ Usage

1. **Launch the application**
   ```bash
   streamlit run app.py
   ```

2. **Select a movie** from the dropdown menu containing 5,000+ movies

3. **Click "Recommend"** to get 5 similar movie suggestions

4. **Explore recommendations** and repeat with different movies

## 📊 Dataset Information

The project uses the **TMDb 5000 Movie Dataset** which includes:

- **Movies Dataset**: 20 features including budget, genres, keywords, overview, production companies, etc.
- **Credits Dataset**: Cast and crew information for each movie
- **Data Size**: 5,000 movies with comprehensive metadata
- **Data Source**: The Movie Database (TMDb)

### Key Features Used for Recommendations:
- **Genres**: Movie categories (Action, Comedy, Drama, etc.)
- **Keywords**: Plot keywords and themes
- **Cast**: Main actors and actresses
- **Crew**: Directors and key crew members
- **Overview**: Movie plot summaries

## 🧠 Machine Learning Approach

### Content-Based Filtering
The system uses content-based filtering which:
- Analyzes movie features and attributes
- Creates feature vectors for each movie
- Calculates similarity between movies
- Doesn't require user rating history
- Provides consistent recommendations

### Similarity Algorithm
- **Cosine Similarity**: Measures the cosine of the angle between feature vectors
- **Range**: 0 (completely different) to 1 (identical)
- **Advantages**: Effective for high-dimensional data, handles varying feature magnitudes

## 🔧 Technical Details

### Dependencies
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning library (for similarity calculations)
- **Pickle**: Object serialization for model persistence

### Performance Optimizations
- **Precomputed Similarity Matrix**: Eliminates real-time calculation overhead
- **Pickle Files**: Fast loading of processed data
- **Efficient Data Structures**: Optimized for memory usage and speed

## 📈 Future Enhancements

- [ ] **Hybrid Recommendation System**: Combine content-based and collaborative filtering
- [ ] **Movie Posters**: Display movie posters using TMDb API
- [ ] **User Ratings**: Add user rating functionality
- [ ] **Advanced Filters**: Filter by genre, year, rating, etc.
- [ ] **Movie Details**: Show detailed movie information
- [ ] **User Profiles**: Save user preferences and history
- [ ] **Batch Recommendations**: Get recommendations for multiple movies
- [ ] **Real-time Updates**: Connect to live movie databases

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

For questions, suggestions, or issues, please:
- Open an issue on GitHub
- Contact the project maintainer

## 🙏 Acknowledgments

- **The Movie Database (TMDb)** for providing the comprehensive movie dataset
- **Streamlit** team for the amazing web framework
- **Scikit-learn** contributors for machine learning tools
- **Open source community** for various libraries and tools used

---

⭐ **Star this repository if you find it helpful!** ⭐

*Built with ❤️ using Python and Streamlit*