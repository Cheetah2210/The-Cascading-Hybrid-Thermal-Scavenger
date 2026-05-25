def calculate_zt(seebeck, electrical_cond, thermal_cond, t_avg):
    """Computes the dimensionless Figure of Merit (ZT) for a TEG material."""
    return (max(0.0, seebeck)**2 * electrical_cond * t_avg) / thermal_cond

def teg_stage_efficiency(t_hot, t_cold, zt_avg):
    """Calculates maximum efficiency of a TEG stage under matched load conditions."""
    tc_th = t_cold / t_hot
    carnot = 1.0 - tc_th
    m_factor = np.sqrt(1.0 + zt_avg)
    
    # Standard engineering efficiency equation for TEGs
    efficiency = carnot * ((m_factor - 1) / (m_factor + tc_th))
    return efficiency
