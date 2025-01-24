const destinationContainer = document.getElementById('destination-container');

function display(cond, val) {
  fetchDestinations(cond, val)
    .then(destinations => {
      destinationContainer.innerHTML = "";
      destinations.forEach(destination => {
        const destinationCard = createDestinationCard(destination);
        destinationContainer.appendChild(destinationCard);
      });
    })
    .catch(error => {
      console.error('Error fetching destinations:', error);
    });
}

let travelDestinationsArray = [
  {
    destination: "Mumbai",
    country: "Maharastra",
    rating: 4.5,
    days: 7,
    image: "https://media.istockphoto.com/id/539018660/photo/taj-mahal-hotel-and-gateway-of-india.jpg?s=612x612&w=0&k=20&c=L1LJVrYMS8kj2rJKlQMcUR88vYoAZeWbYIGkcTo6QV0="
  },
  {
    destination: "Panji",
    country: "Goa",
    rating: 4.8,
    days: 5,
    image: "https://static.toiimg.com/thumb/52501011/Exploring-Panajithe-capital-of-Goa.jpg?width=1200&height=900"
  },
  {
    destination: "Indore",
    country: "Madhya Pradesh",
    rating: 4.7,
    days: 4,
    image: "https://media.istockphoto.com/id/539001564/photo/rajwada-palace-indore.jpg?s=612x612&w=0&k=20&c=ihbWY77GKzZXNmYfvz3dUDpZissBxxcrfSDSMSqa548="
  },
  {
    destination: "Mysore",
    country: "Karnataka",
    rating: 4.9,
    days: 6,
    image: "https://cdn.pixabay.com/photo/2020/09/17/18/10/palace-5579991_1280.jpg"
  },
  {
    destination: "Jaipur",
    country: "Rajasthan",
    rating: 4.6,
    days: 5,
    image: "https://static.independent.co.uk/s3fs-public/thumbnails/image/2018/08/14/09/jaipur-main.jpg?width=1200"
  },
  {
    destination: "Ahmedababad",
    country: "Gujarat",
    rating: 4.8,
    days: 8,
    image: "data:image/jpeg;base64,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"
  },
  {
    destination: "Chennai",
    country: "Tamil Nadu",
    rating: 4.7,
    days: 6,
    image: "https://media.istockphoto.com/id/1226340114/photo/puratchi-thalaivar-dr-mgr-central-railway-station-chennai-central-railway-station-india.jpg?s=612x612&w=0&k=20&c=lZjBnWBBoLiApWZUUWP1Vl3XAVdKjYMcgGpItXv_L14="
  }
];

async function fetchDestinations(cond, val) {
  return travelDestinationsArray.filter(destination => destination[cond].toLowerCase() === val.toLowerCase());
}

function createDestinationCard(destination) {
  const card = document.createElement('div');
  card.classList.add('product-destination-card');

  card.innerHTML = `
    <div class="destination-image" style="height:70%">
        <img src="${destination.image}" alt="${destination.destination}" />
        <div class="bookmark-icon">
            <img src="./public/494568.png" />
        </div>
    </div>
    <div class="product-card-description-bar">
        <div class="left-description">
            <h3 class="country-name">${destination.destination}</h3>
            <div class="destination-info">
                <span class="destination-name">${destination.country}</span>
            </div>
        </div>
        <div class="right-description">
            <div class="rating-container">${destination.rating}
            <span class="rating-star active">★</span>
            </div>
            <span class="days">${destination.days} days</span>
        </div>
    </div>
  `;

  card.addEventListener('click', function () {
    navigateToBookings(destination);
  });

  return card;
}

function navigateToBookings(destination) {
  const queryString = `?destination=${encodeURIComponent(destination.destination)}&country=${encodeURIComponent(destination.country)}`;
  window.location.href = `booking1.html${queryString}`;
}

document.addEventListener('DOMContentLoaded', function () {
  const itemsPerPage = 7; // Adjust the number of items per page
  let currentPage = 1;

  const totalPages = Math.ceil(travelDestinationsArray.length / itemsPerPage);

  function displayDestinations(page) {
    const startIdx = (page - 1) * itemsPerPage;
    const endIdx = startIdx + itemsPerPage;
    const currentDestinations = travelDestinationsArray.slice(startIdx, endIdx);

    destinationContainer.innerHTML = ''; // Clear previous content

    currentDestinations.forEach(destination => {
      const destinationCard = createDestinationCard(destination);
      destinationContainer.appendChild(destinationCard);
    });
  }

  function updatePaginationButtons() {
    document.getElementById('prev-btn').disabled = currentPage === 1;
    document.getElementById('next-btn').disabled = currentPage === totalPages;

    const pagesContainer = document.getElementById('pages-container');
    pagesContainer.innerHTML = '';

    for (let i = 1; i <= totalPages; i++) {
      const pageBtn = document.createElement('button');
      pageBtn.innerText = i;
      pageBtn.addEventListener('click', function () {
        currentPage = i;
        displayDestinations(currentPage);
        updatePaginationButtons();
      });

      if (i === currentPage) {
        pageBtn.classList.add('active');
      }

      pagesContainer.appendChild(pageBtn);
    }
  }

  // Initial display
  displayDestinations(currentPage);
  updatePaginationButtons();
});

function displayRating(container, value) {
  for (let i = 1; i <= 5; i++) {
    const star = document.createElement('span');
    star.className = 'rating-star ' + (i <= value ? 'active' : '');
    star.innerHTML = '&#9733;';
    container.appendChild(star);
  }
}

let ratingsort = document.getElementById("ratingsort");
let myDropdown = document.getElementById("myDropdown");
let myInput = document.getElementById("myInput");

// 
let filternow = document.getElementById("filternow");
filternow.addEventListener('click', (e) => {
  console.log(myDropdown.value, myInput.value);
  display(myDropdown.value, myInput.value);
});

display();
