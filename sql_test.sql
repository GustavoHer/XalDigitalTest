-- 1
-- en la descripción del ejercicio dice nombre_aerolinea en la tabla aeropuertos
-- pero supongo es nombre_aeropuerto
SELECT a.nombre_aeropuerto
FROM aeropuertos a
JOIN vuelos v ON a.id_aeropuerto = v.id_aeropuerto
WHERE YEAR(v.DIA) = YEAR(CURRENT_DATE)
GROUP BY a.id_aeropuerto, a.nombre_aeropuerto
ORDER BY COUNT(*) DESC
LIMIT 1;

-- 2
SELECT ae.nombre_aerolinea
FROM aerolineas ae
JOIN vuelos v ON ae.id_aerolinea = v.id_aerolinea
WHERE YEAR(v.DIA) = YEAR(CURRENT_DATE)
GROUP BY ae.id_aerolinea, ae.nombre_aerolinea
ORDER BY COUNT(*) DESC
LIMIT 1;

-- 3
SELECT DATE(v.DIA) AS fecha, COUNT(*) AS cantidad_vuelos
FROM vuelos v
GROUP BY DATE(v.DIA)
ORDER BY COUNT(*) DESC
LIMIT 1;

--4
SELECT ae.nombre_aerolinea
FROM aerolineas ae
JOIN vuelos v ON ae.id_aerolinea = v.id_aerolinea
GROUP BY ae.id_aerolinea, ae.nombre_aerolinea, DATE(v.DIA)
HAVING COUNT(*) > 2
