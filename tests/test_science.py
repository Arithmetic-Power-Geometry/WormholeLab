import math
import numpy as np
from wormholelab.science import (
    metric_check, kerr_horizons, structural_separation, weak_field_deflection,
    synthetic_ring, precessing_orbit, ringdown_signal, gaussian_loglike,
    scalar_model_evidence, osct_bayes_factor, whiten_residual,
    joint_shared_parameter_evidence, falsification_result, evidence_level,
)

def test_morris_thorne_check():
    c=metric_check("Morris–Thorne wormhole",r0=2.0,exponent=1.0)
    assert c.throat and not c.horizon and c.flare_out

def test_kerr_horizons():
    rp,rm=kerr_horizons(1.0,.5)
    assert rp>rm>0

def test_structural_separation_selects_minimum():
    routes=[
        {"name":"long","time":10,"energy":5,"risk":0,"robustness":1,"admissible":True},
        {"name":"short","time":3,"energy":2,"risk":0,"robustness":.8,"admissible":True},
    ]
    r=structural_separation(100,routes,{"time":1,"energy":1,"risk":1})
    assert r["best_route"]=="short" and r["Dop"]==5 and r["N_gamma"]==2

def test_no_admissible_route_is_infinite():
    r=structural_separation(5,[{"name":"x","admissible":False}])
    assert math.isinf(r["Dop"]) and r["N_gamma"]==0

def test_deflection_positive():
    assert weak_field_deflection(8,1)==0.5

def test_synthetic_ring_shape():
    im=synthetic_ring(size=64)
    assert im.shape==(64,64) and np.all(im>=0)

def test_orbit_shape():
    x,y,t=precessing_orbit(n=250)
    assert len(x)==len(y)==len(t)==250 and np.isfinite(x).all()

def test_ringdown_echo_changes_signal():
    t=np.linspace(0,50,500)
    a=ringdown_signal(t)
    b=ringdown_signal(t,echo_delay=12)
    assert np.max(np.abs(a-b))>0

def test_gaussian_loglike_prefers_truth():
    d=np.array([1.,2.,3.])
    assert gaussian_loglike(d,d,.1)>gaussian_loglike(d,d+1,.1)

def test_scalar_evidence_recovers_parameter():
    x=np.linspace(-1,1,40); truth=.25; y=1+truth*x
    grid=np.linspace(-.5,.5,301)
    res=scalar_model_evidence(y,x,.05,lambda x,t:1+t*x,grid)
    assert abs(res["posterior_mean"]-truth)<.03

def test_osct_prefers_injected_channel():
    rng=np.random.default_rng(4); t=np.linspace(0,80,800); sigma=.03
    y=ringdown_signal(t,echo_delay=20,echo_fraction=.25)+rng.normal(0,sigma,len(t))
    r=osct_bayes_factor(t,y,sigma)
    assert r["logB_OS"]>0 and abs(r["best_delay"]-20)<2

def test_whitening():
    d=np.array([1.,2.,4.]); m=np.array([1.,2.,3.]); r,w=whiten_residual(d,m,np.eye(3))
    assert np.allclose(r,w,atol=1e-8)

def test_joint_parameter():
    grid=np.linspace(0,1,1001); r=joint_shared_parameter_evidence([(0.5,.05),(0.52,.06)],grid)
    assert .49<r["shared_mean"]<.53 and r["shared_sd"]<.06

def test_falsification():
    assert falsification_result(10,10.2,.1,.2)["status"].startswith("SUPPORTED")
    assert falsification_result(10,11,.1,.2)["status"].startswith("FAILED")

def test_evidence_ladder_is_cumulative():
    assert evidence_level(True,True,True,True,True)==5
    assert evidence_level(False,True,True,True,True)==0
