import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [prediction, setPrediction] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setPrediction("");
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please select an audio file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      const res = await axios.post("http://127.0.0.1:8000/predict", formData);
      setPrediction(res.data.prediction || "Error");
    } catch (err) {
      console.error(err);
      setPrediction("Upload failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      
      {/* LEFT IMAGE */}
      <div style={styles.left}>
        <div style={styles.overlay}>
          <h1 style={styles.brand}>SoundSense</h1>
          <p style={styles.tagline}>
            Intelligent Audio Event Detection
          </p>
        </div>
      </div>

      {/* RIGHT CARD */}
      <div style={styles.right}>
        <div style={styles.card}>
          <h2 style={styles.heading}>Upload Audio</h2>
          <p style={styles.subtext}>
            Upload a sound file to detect the event
          </p>

          <label style={styles.fileLabel}>
            🎵 Choose Audio File
            <input
              type="file"
              accept=".wav,audio/*"
              onChange={handleFileChange}
              style={{ display: "none" }}
            />
          </label>

          {file && (
            <p style={styles.filename}>Selected: {file.name}</p>
          )}

          <button onClick={handleUpload} style={styles.button}>
            {loading ? "Analyzing..." : "Upload & Predict"}
          </button>

          {prediction && (
            <div style={styles.result}>
              <strong>Prediction:</strong> {prediction}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;


const styles = {
  container: {
    display: "flex",
    height: "100vh",
    fontFamily: "'Inter', sans-serif",
  },

  left: {
    flex: 1,
    backgroundImage:
      "url('https://images.unsplash.com/photo-1511379938547-c1f69419868d')",
    backgroundSize: "cover",
    backgroundPosition: "center",
    position: "relative",
  },

  overlay: {
    position: "absolute",
    inset: 0,
    background: "rgba(0,0,0,0.45)",
    color: "#fff",
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    paddingLeft: "80px",
  },

  brand: {
    fontSize: "42px",
    fontWeight: 600,
    letterSpacing: "0.5px",
  },

  tagline: {
    marginTop: "8px",
    fontSize: "15px",
    opacity: 0.85,
  },

  right: {
    flex: 1,
    background: "#f5f3ef", // warm beige
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
  },

  card: {
    width: "380px",
    background: "#ffffff",
    padding: "35px",
    borderRadius: "12px",
    boxShadow: "0 8px 25px rgba(0,0,0,0.08)",
    textAlign: "center",
  },

  heading: {
    marginBottom: "8px",
    fontWeight: 600,
  },

  subtext: {
    fontSize: "14px",
    color: "#777",
    marginBottom: "20px",
  },

  fileLabel: {
    display: "inline-block",
    padding: "10px 18px",
    background: "#ece7df",
    borderRadius: "6px",
    cursor: "pointer",
    fontSize: "14px",
    transition: "0.2s",
  },

  filename: {
    fontSize: "13px",
    marginTop: "6px",
    color: "#555",
  },

  button: {
    width: "100%",
    marginTop: "20px",
    padding: "12px",
    background: "#6b5cff",
    color: "#fff",
    border: "none",
    borderRadius: "6px",
    cursor: "pointer",
    fontSize: "15px",
    fontWeight: 500,
  },

  result: {
    marginTop: "18px",
    padding: "12px",
    background: "#f0f0f0",
    borderRadius: "6px",
    fontSize: "14px",
  },
};