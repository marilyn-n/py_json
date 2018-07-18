const vacancies = [
  
  { 
    abilities: ['nice', 'dad', 'cool'],
    benefits: ['money', 'more', 'money'],
    quantity: 2,
  },
  { 
    abilities: ['nice', 'dad', 'cool'],
    benefits: ['money', 'more', 'money'],
    quantity: 3,
  },
  { 
    abilities: ['nice', 'dad', 'cool'],
    benefits: ['money', 'more', 'money'],
    quantity: 5,
  },
  { 
    abilities: ['nice', 'dad', 'cool'],
    benefits: ['money', 'more', 'money'],
    quantity: 8,
  },
  { 
    abilities: ['nice', 'dad', 'cool'],
    benefits: ['money', 'more', 'money'],
    quantity: 2,
  },
  { 
    abilities: ['nice', 'dad', 'cool'],
    benefits: ['money', 'more', 'money'],
    quantity: 3,
  },
  { 
    abilities: ['nice', 'dad', 'cool'],
    benefits: ['money', 'more', 'money'],
    quantity: 5,
  },

];

const frequencies = vacancies.reduce( (prevResult, current) => {
  const position = prevResult.map( item => item.quantity)
    .indexOf(current.quantity);

  position === -1 
  ? prevResult.push({quantity: current.quantity, vacancyCount: 1})
  : (prevResult[position]).vacancyCount++
  return prevResult;
}, []);

console.log(frequencies);


frequencies.map( (item) => {
//   const isPlural = item.vacancyCount === 1;
//  const msg = isPlural 
const msg = `There are ${item.vacancyCount} vacancies with ${item.quantity} candidates`
//  : `There is 1 vacancy with ${item.quantity} candidates`
console.log(msg)
});


// output: Hay 2 vacantes con 3 candidatos
// {quantity: 3, vacancyCount: 2 }
