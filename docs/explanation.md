Para resolver el problema planteado se va a aplicar el concepto de cuadratura Gaussiana para integración utilizando los polinomios de Legendre. La idea principal, la fórmula de la cuadratura Gaussiana está dada por: 

$$
\int_{a}^{b}f(x)dx \approx \sum_{k=1}^{N}w_kf(x_k)
$$
donde $w_k$ son los pesos y x_k son los puntos de muestreo.

En la cuadratura Gaussiana, los puntos de muestreo se escogen de manera no equidistantes. Esto introduce más grados de libetad para la misma discretización en $N$ subregiones. 

Es exacta para un polinomio de orden $2N-1$. 
