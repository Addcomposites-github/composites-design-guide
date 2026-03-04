"""Pydantic models for all API request and response types.

These schemas define the contract between the frontend and backend.
All responses use camelCase-compatible field names so the JSON payloads
are clean for JavaScript consumption.
"""

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Analysis (Photo-to-Plan)
# ---------------------------------------------------------------------------

class AnalysisRequest(BaseModel):
    """Request body for the /api/analyze endpoint."""

    part_description: str = Field(
        ...,
        description="Plain-language description of the part to be manufactured.",
        min_length=3,
        examples=["Carbon fibre bicycle fork with aero cross-section"],
    )
    intended_use: str = Field(
        ...,
        description="How the part will be used and key load cases.",
        min_length=3,
        examples=["Road cycling, rider weight up to 100 kg, pothole impacts"],
    )
    skill_level: Optional[str] = Field(
        default="beginner",
        description="Composites experience level of the builder.",
        pattern="^(beginner|intermediate|advanced)$",
    )
    photo_base64: Optional[str] = Field(
        default=None,
        description="Base64-encoded image of the part or a similar reference part.",
    )


class AnalysisResponse(BaseModel):
    """Full analysis result returned by the /api/analyze endpoint."""

    part_analysis: Dict[str, Any] = Field(
        default_factory=dict,
        description="Geometry type, dimensions, curvature, complexity, load paths.",
    )
    material_recommendation: Dict[str, Any] = Field(
        default_factory=dict,
        description="Fibre type, form, resin system, reasoning.",
    )
    laminate_design: Dict[str, Any] = Field(
        default_factory=dict,
        description="Stacking sequence, number of plies, thickness, reinforcements.",
    )
    manufacturing_plan: Dict[str, Any] = Field(
        default_factory=dict,
        description="Process, steps, materials, consumables, tooling notes.",
    )
    cost_estimate: Dict[str, Any] = Field(
        default_factory=dict,
        description="Material, labour, tooling, consumables, total cost.",
    )
    risk_assessment: Dict[str, Any] = Field(
        default_factory=dict,
        description="Failure modes, inspection points, safety factors, common defects.",
    )
    report_markdown: str = Field(
        default="",
        description="Full markdown report combining all sections.",
    )


# ---------------------------------------------------------------------------
# Materials
# ---------------------------------------------------------------------------

class MaterialQuery(BaseModel):
    """Query parameters for material search."""

    query: str = Field(
        ...,
        description="Search term: material name, fibre type, grade, or resin family.",
        min_length=1,
        examples=["carbon epoxy", "T700", "glass"],
    )


class MaterialResponse(BaseModel):
    """Response for material search."""

    materials: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="List of matching material records.",
    )
    count: int = Field(
        default=0,
        description="Number of matching materials.",
    )


# ---------------------------------------------------------------------------
# Processes
# ---------------------------------------------------------------------------

class ProcessRecommendationRequest(BaseModel):
    """Request body for process recommendation."""

    part_size_m2: float = Field(
        ...,
        gt=0,
        description="Approximate part surface area in square metres.",
    )
    annual_volume: int = Field(
        ...,
        gt=0,
        description="Expected annual production volume.",
    )
    performance_class: str = Field(
        ...,
        description="Required performance level: hobby, structural, or aerospace.",
        pattern="^(hobby|structural|aerospace)$",
    )
    geometry_type: str = Field(
        ...,
        description="Part geometry type.",
        pattern="^(flat|single_curve|double_curve|axisymmetric|constant_cross_section)$",
    )


class ProcessRecommendationResponse(BaseModel):
    """Ranked list of recommended processes."""

    recommendations: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="Processes ranked by suitability score.",
    )


# ---------------------------------------------------------------------------
# Cost Estimation
# ---------------------------------------------------------------------------

class CostEstimateRequest(BaseModel):
    """Request body for cost estimation."""

    fibre_type: str = Field(
        ...,
        description="Fibre / material type, e.g. 'carbon', 'T700', 'glass'.",
    )
    process: str = Field(
        ...,
        description="Manufacturing process ID or name.",
    )
    part_weight_kg: float = Field(
        ...,
        gt=0,
        description="Estimated finished part weight in kilograms.",
    )
    number_of_plies: int = Field(
        ...,
        gt=0,
        description="Number of plies in the laminate.",
    )
    annual_volume: int = Field(
        ...,
        gt=0,
        description="Annual production volume for tooling amortization.",
    )


class CostEstimateResponse(BaseModel):
    """Per-part cost breakdown."""

    material_cost: float = Field(description="Material cost per part (USD).")
    labour_cost: float = Field(description="Labour cost per part (USD).")
    tooling_cost: float = Field(description="Amortized tooling cost per part (USD).")
    consumables_cost: float = Field(description="Consumables cost per part (USD).")
    total_cost: float = Field(description="Total cost per part (USD).")
    breakdown_notes: List[str] = Field(
        default_factory=list,
        description="Human-readable breakdown of each cost component.",
    )
    disclaimer: str = Field(
        default="",
        description="Standard cost-estimate disclaimer.",
    )


# ---------------------------------------------------------------------------
# Knowledge Base Search
# ---------------------------------------------------------------------------

class SearchRequest(BaseModel):
    """Query for knowledge base search."""

    query: str = Field(
        ...,
        description="Natural language search query.",
        min_length=1,
    )
    top_n: Optional[int] = Field(
        default=5,
        ge=1,
        le=20,
        description="Number of results to return (default 5, max 20).",
    )


class SearchResponse(BaseModel):
    """Knowledge base search results."""

    results: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="Ranked search results with scores and metadata.",
    )
    count: int = Field(
        default=0,
        description="Number of results returned.",
    )


# ---------------------------------------------------------------------------
# Stacking Rule Check
# ---------------------------------------------------------------------------

class StackingCheckRequest(BaseModel):
    """Request body for stacking rule verification."""

    angles: List[float] = Field(
        ...,
        description="Ply angles in degrees, top to bottom.",
        min_length=1,
        examples=[[0, 45, -45, 90, 90, -45, 45, 0]],
    )
    max_consecutive: Optional[int] = Field(
        default=4,
        ge=1,
        le=10,
        description="Max allowed consecutive same-angle plies (default 4).",
    )


class StackingCheckResponse(BaseModel):
    """Results of stacking rule checks."""

    results: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="Individual rule check results.",
    )
    all_passed: bool = Field(
        default=False,
        description="True if every rule passed.",
    )


# ---------------------------------------------------------------------------
# Sandwich Panel Design
# ---------------------------------------------------------------------------

class SandwichLoadType(str, Enum):
    """Supported loading conditions for sandwich panel analysis."""

    uniform_pressure = "uniform_pressure"
    point_load = "point_load"
    bending = "bending"


class SandwichAnalysisRequest(BaseModel):
    """Request body for sandwich panel analysis."""

    face_thickness_mm: float = Field(
        ...,
        gt=0,
        description="Thickness of each face sheet in millimetres.",
        examples=[1.0],
    )
    core_thickness_mm: float = Field(
        ...,
        gt=0,
        description="Thickness of the core material in millimetres.",
        examples=[20.0],
    )
    face_E_GPa: float = Field(
        ...,
        gt=0,
        description="Young's modulus of the face sheet material in GPa.",
        examples=[70.0],
    )
    face_sigma_ult_MPa: float = Field(
        ...,
        gt=0,
        description="Ultimate strength of the face sheet material in MPa.",
        examples=[600.0],
    )
    core_material_id: str = Field(
        ...,
        description=(
            "Identifier for the core material from the built-in database, "
            "e.g. 'nomex_honeycomb_48', 'pvc_foam_80', 'balsa_150'."
        ),
        examples=["nomex_honeycomb_48"],
    )
    panel_length_mm: float = Field(
        ...,
        gt=0,
        description="Panel span (simply-supported direction) in mm.",
        examples=[500.0],
    )
    panel_width_mm: float = Field(
        ...,
        gt=0,
        description="Panel width in mm.",
        examples=[300.0],
    )
    load_type: SandwichLoadType = Field(
        ...,
        description=(
            "Type of loading: 'uniform_pressure' (Pa), "
            "'point_load' (N), or 'bending' (N/m line load)."
        ),
        examples=["uniform_pressure"],
    )
    applied_load: float = Field(
        ...,
        gt=0,
        description=(
            "Load magnitude.  Units depend on load_type: "
            "Pa for uniform_pressure, N for point_load, N/m for bending."
        ),
        examples=[5000.0],
    )


class SandwichAnalysisResponse(BaseModel):
    """Full analysis result for a sandwich panel."""

    stiffness: Dict[str, Any] = Field(
        default_factory=dict,
        description=(
            "Bending stiffness (D), shear stiffness (S), "
            "stiffness-to-weight ratio, total thickness."
        ),
    )
    weight_per_m2_kg: float = Field(
        default=0.0,
        description="Total areal weight including faces, core, and adhesive (kg/m2).",
    )
    cost_per_m2_usd: float = Field(
        default=0.0,
        description="Estimated cost per square metre (USD/m2).",
    )
    failure_checks: List[Dict[str, Any]] = Field(
        default_factory=list,
        description=(
            "List of failure-mode checks.  Each entry has 'mode', "
            "'status' (PASS/FAIL/N/A), 'margin', and 'detail'."
        ),
    )
    overall_pass: bool = Field(
        default=False,
        description="True if every applicable failure mode passed.",
    )
    design_summary: str = Field(
        default="",
        description="Human-readable summary of the design and its assessment.",
    )


class SandwichOptimizationRequest(BaseModel):
    """Request body for sandwich panel optimisation."""

    face_E_GPa: float = Field(
        ...,
        gt=0,
        description="Young's modulus of the face sheet material in GPa.",
        examples=[70.0],
    )
    face_sigma_ult_MPa: float = Field(
        ...,
        gt=0,
        description="Ultimate strength of the face sheet material in MPa.",
        examples=[600.0],
    )
    panel_length_mm: float = Field(
        ...,
        gt=0,
        description="Panel span (simply-supported direction) in mm.",
        examples=[500.0],
    )
    panel_width_mm: float = Field(
        ...,
        gt=0,
        description="Panel width in mm.",
        examples=[300.0],
    )
    load_type: SandwichLoadType = Field(
        ...,
        description=(
            "Type of loading: 'uniform_pressure' (Pa), "
            "'point_load' (N), or 'bending' (N/m line load)."
        ),
        examples=["uniform_pressure"],
    )
    applied_load: float = Field(
        ...,
        gt=0,
        description=(
            "Load magnitude.  Units depend on load_type: "
            "Pa for uniform_pressure, N for point_load, N/m for bending."
        ),
        examples=[5000.0],
    )
    target_stiffness_Nm: Optional[float] = Field(
        default=None,
        gt=0,
        description=(
            "Minimum required bending stiffness D in N-mm2/mm.  "
            "Leave empty to skip this constraint."
        ),
    )
    max_weight_kg_m2: Optional[float] = Field(
        default=None,
        gt=0,
        description=(
            "Maximum allowable areal weight in kg/m2.  "
            "Leave empty to skip this constraint."
        ),
    )


class CoreMaterialResponse(BaseModel):
    """Response for a single core material."""

    id: str = Field(description="Core material identifier.")
    name: str = Field(description="Human-readable name.")
    density_kg_m3: float = Field(description="Core density (kg/m3).")
    shear_strength_MPa: float = Field(description="Core shear strength (MPa).")
    shear_modulus_MPa: float = Field(description="Core shear modulus (MPa).")
    compressive_strength_MPa: float = Field(
        description="Core flatwise compressive strength (MPa)."
    )
    compressive_modulus_MPa: float = Field(
        description="Core flatwise compressive modulus (MPa)."
    )
    cell_size_mm: float = Field(
        description="Honeycomb cell size in mm (0 for foam/balsa cores)."
    )
    cost_usd_per_m2: float = Field(
        description="Approximate cost per square metre (USD/m2)."
    )


# ---------------------------------------------------------------------------
# CLT (Classical Lamination Theory)
# ---------------------------------------------------------------------------

class PlyDefinition(BaseModel):
    """Single ply definition for CLT calculations."""

    angle: float = Field(
        ...,
        description="Ply angle in degrees.",
        examples=[0, 45, -45, 90],
    )
    thickness_mm: float = Field(
        ...,
        gt=0,
        description="Ply thickness in millimetres.",
        examples=[0.125, 0.13, 0.2],
    )
    E1_GPa: float = Field(
        ...,
        gt=0,
        description="Longitudinal (fibre direction) modulus in GPa.",
        examples=[135.0, 181.0],
    )
    E2_GPa: float = Field(
        ...,
        gt=0,
        description="Transverse modulus in GPa.",
        examples=[9.0, 10.3],
    )
    G12_GPa: float = Field(
        ...,
        gt=0,
        description="In-plane shear modulus in GPa.",
        examples=[5.0, 7.17],
    )
    nu12: float = Field(
        ...,
        gt=0,
        lt=1,
        description="Major Poisson's ratio (dimensionless).",
        examples=[0.3, 0.28],
    )


class LaminateLoads(BaseModel):
    """Applied loads for CLT analysis."""

    Nx: float = Field(default=0.0, description="In-plane force resultant, x-direction (N/m).")
    Ny: float = Field(default=0.0, description="In-plane force resultant, y-direction (N/m).")
    Nxy: float = Field(default=0.0, description="In-plane shear force resultant (N/m).")
    Mx: float = Field(default=0.0, description="Bending moment resultant, x-direction (N*m/m).")
    My: float = Field(default=0.0, description="Bending moment resultant, y-direction (N*m/m).")
    Mxy: float = Field(default=0.0, description="Twisting moment resultant (N*m/m).")


class CalculateLaminateRequest(BaseModel):
    """Request body for /api/calculate-laminate."""

    layup: List[PlyDefinition] = Field(
        ...,
        min_length=1,
        description="List of ply definitions from top to bottom.",
    )
    loads: Optional[LaminateLoads] = Field(
        default=None,
        description="Applied loads (optional). If provided, ply stresses are calculated.",
    )


class CalculateLaminateResponse(BaseModel):
    """Response from /api/calculate-laminate."""

    engine: str = Field(
        description="CLT engine used: 'composipy' or 'numpy_fallback'.",
    )
    num_plies: int = Field(description="Number of plies in the laminate.")
    total_thickness_mm: float = Field(description="Total laminate thickness in mm.")
    A_matrix: List[List[float]] = Field(
        description="3x3 extensional stiffness matrix A (N/m).",
    )
    B_matrix: List[List[float]] = Field(
        description="3x3 coupling stiffness matrix B (N).",
    )
    D_matrix: List[List[float]] = Field(
        description="3x3 bending stiffness matrix D (N*m).",
    )
    ABD_matrix: List[List[float]] = Field(
        description="Full 6x6 ABD stiffness matrix.",
    )
    effective_moduli: Dict[str, float] = Field(
        description="Effective engineering constants: Ex_GPa, Ey_GPa, Gxy_GPa, nuxy, nuyx.",
    )
    ply_stresses: Optional[List[Dict[str, Any]]] = Field(
        default=None,
        description="Per-ply stresses and strains (only if loads were provided).",
    )
    midplane_strains: Optional[Dict[str, float]] = Field(
        default=None,
        description="Midplane strains and curvatures (only if loads were provided).",
    )


class MaterialStrengths(BaseModel):
    """Material strength values for failure analysis."""

    Xt_MPa: float = Field(..., gt=0, description="Longitudinal tensile strength (MPa).")
    Xc_MPa: float = Field(..., gt=0, description="Longitudinal compressive strength (MPa).")
    Yt_MPa: float = Field(..., gt=0, description="Transverse tensile strength (MPa).")
    Yc_MPa: float = Field(..., gt=0, description="Transverse compressive strength (MPa).")
    S12_MPa: float = Field(..., gt=0, description="In-plane shear strength (MPa).")


class CheckFailureRequest(BaseModel):
    """Request body for /api/check-failure."""

    layup: List[PlyDefinition] = Field(
        ...,
        min_length=1,
        description="List of ply definitions from top to bottom.",
    )
    strengths: MaterialStrengths = Field(
        ...,
        description="Material strength allowables.",
    )
    loads: LaminateLoads = Field(
        ...,
        description="Applied loads.",
    )
    criterion: str = Field(
        default="max_stress",
        description="Failure criterion: 'max_stress', 'tsai_wu', 'tsai_hill', or 'hashin'.",
        pattern="^(max_stress|tsai_wu|tsai_hill|hashin)$",
    )


class CheckFailureResponse(BaseModel):
    """Response from /api/check-failure."""

    criterion: str = Field(description="Failure criterion used.")
    per_ply_results: List[Dict[str, Any]] = Field(
        description="Failure index and mode for each ply.",
    )
    first_ply_failure: Dict[str, Any] = Field(
        description="Information about the first ply to fail (if any).",
    )
    overall_failed: bool = Field(description="True if any ply has failed.")
    worst_ply_index: int = Field(description="Index of the ply with the highest failure index.")
    worst_failure_index: float = Field(description="Highest failure index across all plies.")
    min_margin_of_safety: Optional[float] = Field(
        description="Minimum margin of safety (1/FI - 1). None if FI is zero.",
    )
    effective_moduli: Dict[str, float] = Field(
        description="Effective engineering constants of the laminate.",
    )


class OptimizeLaminateConstraints(BaseModel):
    """Constraints for laminate optimisation."""

    min_plies: int = Field(default=4, ge=2, description="Minimum number of plies.")
    max_plies: int = Field(default=64, ge=4, le=200, description="Maximum number of plies.")
    allowed_angles: List[float] = Field(
        default=[0, 45, -45, 90],
        description="Allowed ply angles in degrees.",
    )
    symmetry_required: bool = Field(
        default=True,
        description="Whether the laminate must be symmetric.",
    )


class OptimizeLaminateMaterial(BaseModel):
    """Material properties for optimisation (single ply data)."""

    E1_GPa: float = Field(..., gt=0, description="Longitudinal modulus (GPa).")
    E2_GPa: float = Field(..., gt=0, description="Transverse modulus (GPa).")
    G12_GPa: float = Field(..., gt=0, description="In-plane shear modulus (GPa).")
    nu12: float = Field(..., gt=0, lt=1, description="Major Poisson's ratio.")
    thickness_mm: float = Field(..., gt=0, description="Single ply thickness (mm).")


class OptimizeLaminateRequest(BaseModel):
    """Request body for /api/optimize-laminate."""

    loads: LaminateLoads = Field(..., description="Target loads to size for.")
    material: OptimizeLaminateMaterial = Field(..., description="Single-ply material properties.")
    strengths: MaterialStrengths = Field(..., description="Material strength allowables.")
    constraints: Optional[OptimizeLaminateConstraints] = Field(
        default=None,
        description="Optimisation constraints (optional).",
    )


class OptimizeLaminateResponse(BaseModel):
    """Response from /api/optimize-laminate."""

    loads: Dict[str, float] = Field(description="The loads used for optimisation.")
    material: Dict[str, float] = Field(description="The material properties used.")
    strengths: Dict[str, float] = Field(description="The strengths used.")
    num_candidates: int = Field(description="Number of viable laminate candidates found.")
    candidates: List[Dict[str, Any]] = Field(
        description="Viable laminates ranked by thickness (lightest first).",
    )
    recommendation: Optional[Dict[str, Any]] = Field(
        description="The recommended (lightest passing) laminate, or None.",
    )
    note: str = Field(description="Explanatory note about the results.")


# ---------------------------------------------------------------------------
# Bolted Joint Analysis
# ---------------------------------------------------------------------------


class BoltedJointAnalysisRequest(BaseModel):
    """Request body for bolted joint analysis."""

    bolt_diameter_mm: float = Field(
        ...,
        gt=0,
        description="Nominal bolt shank diameter in mm.",
        examples=[6.0],
    )
    hole_diameter_mm: float = Field(
        ...,
        gt=0,
        description=(
            "Drilled hole diameter in mm.  Typically bolt diameter + 0.1 "
            "to 0.2 mm for aerospace clearance fit."
        ),
        examples=[6.15],
    )
    laminate_thickness_mm: float = Field(
        ...,
        gt=0,
        description="Laminate thickness at the joint in mm.",
        examples=[4.0],
    )
    laminate_width_mm: float = Field(
        ...,
        gt=0,
        description=(
            "Strip width for single-bolt, or pitch between bolts for "
            "multi-row analysis, in mm."
        ),
        examples=[36.0],
    )
    edge_distance_mm: float = Field(
        ...,
        gt=0,
        description=(
            "Distance from hole centre to the nearest free edge in the "
            "load direction, in mm."
        ),
        examples=[18.0],
    )
    applied_load_N: float = Field(
        ...,
        gt=0,
        description="Total applied tensile or compressive load through the joint in N.",
        examples=[10000.0],
    )
    bearing_strength_MPa: float = Field(
        ...,
        gt=0,
        description=(
            "Laminate bearing strength in MPa, typically from ASTM D5961 "
            "test data.  Common CFRP values: 400-800 MPa."
        ),
        examples=[600.0],
    )
    tension_strength_MPa: float = Field(
        ...,
        gt=0,
        description=(
            "Open-hole tension (OHT) or filled-hole tension (FHT) "
            "strength of the laminate in MPa."
        ),
        examples=[450.0],
    )
    shear_out_strength_MPa: float = Field(
        ...,
        gt=0,
        description="Shear-out (tear-out) strength of the laminate in MPa.",
        examples=[300.0],
    )
    bypass_ratio: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description=(
            "Fraction of total load that bypasses the fastener (0.0 = all "
            "bearing, 1.0 = all bypass).  Default is 0.0."
        ),
        examples=[0.0],
    )
    num_fasteners: int = Field(
        default=1,
        ge=1,
        le=20,
        description=(
            "Number of fasteners in a row.  Load distribution uses the "
            "spring-analogy method.  Default is 1."
        ),
        examples=[1],
    )


class BoltedJointAnalysisResponse(BaseModel):
    """Full analysis result for a bolted joint."""

    bearing_check: Dict[str, Any] = Field(
        default_factory=dict,
        description=(
            "Bearing stress check: mode, status, applied stress, "
            "allowable, margin of safety, detail."
        ),
    )
    net_tension_check: Dict[str, Any] = Field(
        default_factory=dict,
        description=(
            "Net-tension stress check: mode, status, applied stress, "
            "allowable, margin of safety, detail."
        ),
    )
    shear_out_check: Dict[str, Any] = Field(
        default_factory=dict,
        description=(
            "Shear-out stress check: mode, status, applied stress, "
            "allowable, margin of safety, detail."
        ),
    )
    cleavage_check: Dict[str, Any] = Field(
        default_factory=dict,
        description=(
            "Cleavage geometry check: e/d and w/d ratios against "
            "minimum design rules."
        ),
    )
    bearing_bypass_interaction: Dict[str, Any] = Field(
        default_factory=dict,
        description=(
            "Bearing-bypass interaction envelope check: interaction "
            "index, bearing and bypass ratios."
        ),
    )
    fastener_load_distribution: Dict[str, Any] = Field(
        default_factory=dict,
        description=(
            "Load distribution across fasteners: total load, average "
            "and peak fastener loads, overload factor."
        ),
    )
    geometry_ratios: Dict[str, Any] = Field(
        default_factory=dict,
        description=(
            "Key geometry ratios: d/t, e/d, w/d with recommended ranges."
        ),
    )
    overall_pass: bool = Field(
        default=False,
        description="True if every failure mode check passed.",
    )
    minimum_margin: float = Field(
        default=0.0,
        description="Minimum margin of safety across all checked modes.",
    )
    design_recommendations: List[str] = Field(
        default_factory=list,
        description=(
            "List of design recommendations and warnings based on "
            "geometry ratios and margins."
        ),
    )
    design_summary: str = Field(
        default="",
        description="Human-readable summary of the joint analysis.",
    )


class BoltedJointRecommendRequest(BaseModel):
    """Request body for joint sizing recommendations."""

    applied_load_N: float = Field(
        ...,
        gt=0,
        description="Total applied load through the joint in N.",
        examples=[10000.0],
    )
    laminate_thickness_mm: float = Field(
        ...,
        gt=0,
        description="Laminate thickness at the joint in mm.",
        examples=[4.0],
    )
    material_bearing_strength_MPa: float = Field(
        ...,
        gt=0,
        description="Bearing strength of the laminate in MPa.",
        examples=[600.0],
    )
    safety_factor: float = Field(
        default=1.5,
        gt=0,
        description=(
            "Design safety factor applied to the bearing strength.  "
            "Default is 1.5."
        ),
        examples=[1.5],
    )


class BoltedJointRecommendResponse(BaseModel):
    """Joint sizing recommendation result."""

    recommended_bolts: List[Dict[str, Any]] = Field(
        default_factory=list,
        description=(
            "List of viable bolt options ranked by suitability, each "
            "with diameter, d/t ratio, minimum edge distance, width, "
            "pitch, bearing margin, and shear capacity."
        ),
    )
    design_rules_applied: List[str] = Field(
        default_factory=list,
        description="Design rules that were applied in the recommendation.",
    )
    input_summary: Dict[str, Any] = Field(
        default_factory=dict,
        description=(
            "Summary of the inputs and derived minimum bolt diameter."
        ),
    )
    summary: str = Field(
        default="",
        description="Human-readable recommendation summary.",
    )


class BoltResponse(BaseModel):
    """Response for a single bolt from the fastener database."""

    id: str = Field(description="Bolt identifier (e.g. 'M6').")
    name: str = Field(description="Human-readable name.")
    nominal_diameter_mm: float = Field(description="Nominal shank diameter (mm).")
    max_shear_load_N: float = Field(
        description="Maximum single-shear load capacity (N)."
    )
    max_tension_load_N: float = Field(
        description="Maximum axial tension load capacity (N)."
    )
    weight_g: float = Field(description="Approximate fastener weight (grams).")
    common_use: str = Field(
        description="Typical applications for this bolt size."
    )
