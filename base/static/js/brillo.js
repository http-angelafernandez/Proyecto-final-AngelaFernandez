document.addEventListener('mousemove', function (e) {
    const container = document.getElementById('container');
    const numSparks = 8; 

    for (let i = 0; i < numSparks; i++) {
        const sparkle = document.createElement('div');
        sparkle.classList.add('sparkle');
        
        
        sparkle.style.left = `${e.clientX}px`;
        sparkle.style.top = `${e.clientY}px`;

        
        const xDir = Math.random() < 0.5 ? -1 : 1;
        const yDir = Math.random() < 0.5 ? -1 : 1;

        sparkle.style.setProperty('--x-dir', xDir);
        sparkle.style.setProperty('--y-dir', yDir);


        sparkle.style.width = `${Math.random() * 2 + 2}px`; 
        sparkle.style.height = sparkle.style.width;
        sparkle.style.opacity = Math.random() * 0.5 + 0.5;

        container.appendChild(sparkle);

   
        setTimeout(() => {
            sparkle.remove();
        }, 1500);
    }
});


