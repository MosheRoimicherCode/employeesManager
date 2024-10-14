﻿using System.ComponentModel.DataAnnotations;

namespace Server.Models;

public class Permission
{
    [Key]
    public int Id { get; set; }
    public int FloorLevel { get; set; }
    public string Building { get; set; }

    public Permission(int floorLevel, string building)
    {
        FloorLevel = floorLevel;
        Building = building;
    }

    public override string ToString()
    {
        return $"Levels: {FloorLevel}, Buildings: {Building}";
    }
}
