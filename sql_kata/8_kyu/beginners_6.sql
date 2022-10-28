-- https://www.codewars.com/kata/5e5f09dc0a17be0023920f6f

SELECT capital FROM countries
WHERE continent LIKE 'Afri_a'
AND country LIKE 'E%'
ORDER BY capital ASC
LIMIT 3;