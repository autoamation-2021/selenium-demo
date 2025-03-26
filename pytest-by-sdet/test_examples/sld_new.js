let number = 12345678911011.2222344;

// Format number for U.S. locale
let formatted_number = new Intl.NumberFormat('en-US', {
    style: 'decimal',
    minimumFractionDigits: 2,
    maximumFractionDigits: 2
}).format(number);

console.log(formatted_number);  // Output: 12,345,678,911,011.22