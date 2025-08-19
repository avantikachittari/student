/* Flower buttons */
.button {
    background-color: #f8c8dc;
    border: none;
    padding: 20px;
    border-radius: 50%; /* makes them circular like a flower center */
    font-weight: bold;
    color: #4a4a4a !important;
    text-decoration: none;
    display: inline-block;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
    margin: 20px;
}

/* Petals using pseudo-elements */
.button::before, .button::after {
    content: "";
    position: absolute;
    width: 100%;
    height: 100%;
    background: #f8c8dc;
    border-radius: 50%;
    z-index: -1;
    transition: transform 0.3s ease;
}

/* Petal positions */
.button::before {
    top: -50%;
    left: 0;
}
.button::after {
    left: 50%;
    top: 0;
}

/* Hover effect: bloom like a flower */
.button:hover {
    transform: scale(1.1);
    box-shadow: 0 0 15px #f7b5d4, 0 0 30px #f7b5d4;
}
.button:hover::before {
    transform: translateY(-10px) scale(1.1);
}
.button:hover::after {
    transform: translateX(10px) scale(1.1);
}
