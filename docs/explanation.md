To solve the stated problem, the concept of Gaussian quadrature will be applied for integration using Legendre polynomials. The main idea, the formula of Gaussian quadrature, is given by:

$$
\int_{a}^{b}f(x)dx \approx \sum_{k=1}^{N}w_kf(x_k)
$$
where $w_k$ are the weights and $x_k$ are the sampling points.

In Gaussian quadrature, the sampling points are chosen in a non-equidistant manner. This introduces more degrees of freedom compared to the same discretization into $N$ subregions.

It is exact for a polynomial of order $2N-1$. 
