# Artifacts for "A Comparative Performance Analysis of GPU-Aware MPI Implementations Over the Slingshot-11 Interconnect"

## Software
- **Operating System**: Linux (Cray Shasta)
- **Job Scheduler**: SLURM
- **MPI Libraries**: Cray MPICH v8.1.25,  MPICH v4.1.1,  Open MPI v5.0
- **Compilers**: GNU v11.2.0,  CUDA v11.7, KOKKOS v3.6
- **OSU Microbenchmarks**: Can obtain the latest version with `wget [http://mvapich.cse.ohio-state.edu/download/mvapich/osu-micro-benchmarks-7.2.tar.gz](http://mvapich.cse.ohio-state.edu/download/mvapich/osu-micro-benchmarks-7.2.tar.gz)`. We used OSUMB v7.1.1 for our study, for which you will need to contact the Network-Based Computing Laboratory at Ohio State University as older versions are not available on their website. Use `./configure --enable-cuda` when building with the desired MPI implementation and C compiler enabled.
- **LAMMPS**: v2022.11.03 can be downloaded from [https://www.lammps.org/download.html](https://www.lammps.org/download.html).
- **WarpX**: v23.04 can be downloaded with `git clone [https://github.com/ECP-WarpX/WarpX.git](https://github.com/ECP-WarpX/WarpX.git)`

## Hardware
- **CPU**: x86_64 AMD Epyc Milan
- **GPU**: NVIDIA A100
- **Network**: Slingshot-11

## Scripts and Raw Data
For the sake of simplicity, we included our job scripts, build scripts, and raw data in a public GitHub repository, which can be cloned with `git clone [https://github.com/michael-beebe/p3hpc23_artifacts.git](https://github.com/michael-beebe/p3hpc23_artifacts.git)`.
