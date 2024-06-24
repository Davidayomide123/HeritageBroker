// script.js

const cryptoIcons = {
    bitcoin: 'fab fa-btc',
    ethereum: 'fab fa-ethereum',
    litecoin: 'fab fa-ltc',
    ripple: 'fab fa-xrp',
    cardano: 'fab fa-ada',
    polkadot: 'fas fa-dot-circle',
    stellar: 'fab fa-strl',
    chainlink: 'fab fa-link',
    'bitcoin-cash': 'fab fa-bch',
    uniswap: 'fas fa-uniswap',
    tezos: 'fab fa-tez'
};

async function fetchCryptoData() {
    const response = await fetch('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin,ethereum,litecoin,ripple,cardano,polkadot,stellar,chainlink,bitcoin-cash,uniswap,tezos');
    const data = await response.json();
    return data;
}

async function populateCryptoTable() {
    const table = document.getElementById('crypto-table');
    const cryptoData = await fetchCryptoData();
    cryptoData.forEach(crypto => {
        const row = table.insertRow(-1);
        const symbolCell = row.insertCell(0);
        const priceCell = row.insertCell(1);
        const marketCapCell = row.insertCell(2);
        const changeCell = row.insertCell(3);

        const iconClass = cryptoIcons[crypto.id] || 'fas fa-coins';
        symbolCell.innerHTML = `<i class="${iconClass}"></i> ${crypto.symbol.toUpperCase()}`;
        priceCell.textContent = `$${crypto.current_price.toFixed(2)}`;
        marketCapCell.textContent = `$${crypto.market_cap.toLocaleString()}`;
        changeCell.textContent = `${crypto.price_change_percentage_24h.toFixed(2)}%`;
    });
}

populateCryptoTable();

document.addEventListener('DOMContentLoaded', function() {
    const notificationIcon = document.querySelector('.notification-icon');

    notificationIcon.addEventListener('click', function() {
        notificationIcon.classList.add('vibrate');

        setTimeout(() => {
            notificationIcon.classList.remove('vibrate');
        }, 300);
    });

    const ctx = document.getElementById('investment-chart').getContext('2d');

    const investmentChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
            datasets: [{
                label: 'Investment Growth',
                data: [5000, 10000, 15000, 20000, 25000, 30000, 35000],
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            animation: {
                duration: 2000
            }
        }
    });

    const sidebar = document.getElementById('sidebar');
    const menuToggle = document.getElementById('menu-toggle');
    const closeBtn = document.getElementById('close-btn');

    menuToggle.addEventListener('click', function() {
        sidebar.style.width = '250px';
    });

    closeBtn.addEventListener('click', function() {
        sidebar.style.width = '0';
    });

    window.addEventListener('click', function(event) {
        if (event.target == sidebar) {
            sidebar.style.width = '0';
        }
    });

    const themeToggle = document.getElementById('theme-toggle');

    themeToggle.addEventListener('change',
        function() {
            if (themeToggle.checked) {
                document.body.classList.remove('light-theme');
                document.body.classList.add('dark-theme');
            } else {
                document.body.classList.remove('dark-theme');
                document.body.classList.add('light-theme');
            }
        });

    function showLoadingSpinner() {
        document.getElementById('loading-spinner').style.display = 'flex';
    }

    function hideLoadingSpinner() {
        document.getElementById('loading-spinner').style.display = 'none';
    }

    window.addEventListener('beforeunload',
        showLoadingSpinner);

    document.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', showLoadingSpinner);
    });

    hideLoadingSpinner();

    function updateCurrencyRates() {
        const rates = [{
            currency: 'Bitcoin (BTC)', rate: '$40,000', change: '+5%'
        },
            {
                currency: 'Ethereum (ETH)', rate: '$2,500', change: '-3%'
            },
            {
                currency: 'Litecoin (LTC)', rate: '$150', change: '+2%'
            },
            {
                currency: 'Ripple (XRP)', rate: '$0.90', change: '-1%'
            }];

        rates.forEach((rate, index) => {
            const row = document.querySelectorAll('.currency-table tbody tr')[index];
            row.children[1].textContent = rate.rate;
            row.children[2].textContent = rate.change;

            if (rate.change.startsWith('+')) {
                row.children[2].classList.add('positive-change');
                row.children[2].classList.remove('negative-change');
            } else {
                row.children[2].classList.add('negative-change');
                row.children[2].classList.remove('positive-change');
            }
        });
    }

    setInterval(updateCurrencyRates,
        5000);
});
document.addEventListener('DOMContentLoaded', function() {
    var header = document.getElementById('header');
    var fadeIn = true;

    function animateHeader() {
        if (fadeIn) {
            header.style.opacity = 1;
        } else {
            header.style.opacity = 0;
        }
        fadeIn = !fadeIn;
    }

    setInterval(animateHeader, 2000);
});