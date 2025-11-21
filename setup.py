from pathlib import Path
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

this_dir = Path(__file__).parent

extra_compile_args = {
    "cxx": ["-O3"],
    "nvcc": [
        "-O3",
        "--use_fast_math",
        "-U__CUDA_NO_HALF_OPERATORS__",
        "-U__CUDA_NO_HALF_CONVERSIONS__",
        "-U__CUDA_NO_HALF2_OPERATORS__",
    ],
}

ext_modules = [
    CUDAExtension(
        name="selective_scan_cuda",
        sources=[
            "csrc/selective_scan/selective_scan.cpp",
            "csrc/selective_scan/selective_scan_fwd_fp32.cu",
            "csrc/selective_scan/selective_scan_fwd_fp16.cu",
            "csrc/selective_scan/selective_scan_fwd_bf16.cu",
            "csrc/selective_scan/selective_scan_bwd_fp32_real.cu",
            "csrc/selective_scan/selective_scan_bwd_fp32_complex.cu",
            "csrc/selective_scan/selective_scan_bwd_fp16_real.cu",
            "csrc/selective_scan/selective_scan_bwd_fp16_complex.cu",
            "csrc/selective_scan/selective_scan_bwd_bf16_real.cu",
            "csrc/selective_scan/selective_scan_bwd_bf16_complex.cu",
        ],
        include_dirs=[this_dir / "csrc" / "selective_scan"],
        extra_compile_args=extra_compile_args,
    )
]

setup(
    name="SelectiveSSM",
    version="0.1.0",
    description="Minimal CUDA extension for selective scan",
    author="Lucas Benedetti",
    packages=["SelectiveSSM"],
    ext_modules=ext_modules,
    cmdclass={"build_ext": BuildExtension},
)
