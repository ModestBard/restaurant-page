const heroDiv = document.createElement("div")
heroDiv.classList.add("hero")

const tagLine = document.createElement("h1")
tagLine.innerHTML = "The Cuisine you <br> Never Experienced Before"
tagLine.classList.add("tag-line")
heroDiv.appendChild(tagLine)

const img = document.createElement("img")
img.alt = "hero-image"
img.classList.add("hero-image")

// Import images if using a bundler (e.g., Webpack, Create React App)
import img1 from "./images/hero-image/1.jpg"
import img2 from "./images/hero-image/2.jpg"
import img3 from "./images/hero-image/3.jpg"
import img4 from "./images/hero-image/4.jpg"

// Array of image URLs
const images = [img1, img2, img3, img4]

let currentIndex = 0
img.src = images[currentIndex] // Set initial image
heroDiv.appendChild(img)

// Function to update the image every 5 seconds
const startSlideshow = () => {
  setInterval(() => {
    currentIndex = (currentIndex + 1) % images.length
    img.src = images[currentIndex]
  }, 5000) // 5000 ms = 5 seconds
}

startSlideshow()

export default heroDiv
