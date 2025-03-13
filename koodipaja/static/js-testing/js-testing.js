const personsArray = [
    { id: 1, firstName: "Malcom", lastName: "Reynolds" },
    { id: 2, firstName: "Kaylee", lastName: "Frye" },
    { id: 3, firstName: "Jayne", lastName: "Cobb" }
];

// Returns a new array of objects with a 'fullName' property
const reformatPersons = function (persons) {
    return persons.map(function (person) {
        // Create a new object to store the full name
        const newObj = {};
        newObj["fullName"] = person.firstName + " " + person.lastName;
        // Return our new object
        return newObj;
    });
};

// Call reformatPersons and get a new array of full names
const fullNameArray = reformatPersons(personsArray);

console.log(fullNameArray);
// Output:
// [
//   { fullName: "Malcom Reynolds" },
//   { fullName: "Kaylee Frye" },
//   { fullName: "Jayne Cobb" }
// ]

// The original personsArray remains unchanged
console.log(personsArray);
// Output:
// [
//   { id: 1, firstName: "Malcom", lastName: "Reynolds" },
//   { id: 2, firstName: "Kaylee", lastName: "Frye" },
//   { id: 3, firstName: "Jayne", lastName: "Cobb" }
// ]
